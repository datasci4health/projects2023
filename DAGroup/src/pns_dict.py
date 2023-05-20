import ast
import copy

import pandas as pd


class PnsDictRaw:

    def __init__(self):
        xls = pd.ExcelFile('../data/raw/PNS_2019/dicionario.xlsx')

        def process(df_i):
            df_i = df_i[2:]
            df_i = df_i.dropna(subset=['desc', 'pv', 'pv_desc'], how='all')
            df_i[['cod', 'desc']] = df_i[['cod', 'desc']].ffill()
            df_i['cod'] = df_i['cod'].str.upper()
            return df_i

        df = pd.read_excel(xls, sheet_name='dicionário pns', names=['cod', 'desc', 'pv', 'pv_desc'])
        self.df = process(df)

    def get_df_cod(self, cod):
        return self.df[self.df['cod'] == cod]

    def get_question(self, cod):
        try:
            return self.get_df_cod(cod)['desc'].values[0].strip()
        except:
            return ''

    def get_pv_dict(self, cod):
        dictionary = self.get_df_cod(cod)[['pv', 'pv_desc']].set_index('pv')['pv_desc'].to_dict()

        pv_dict = {}
        for k, v in dictionary.items():
            try:
                pv_dict[int(float(k))] = v.strip()
            except:
                pass

        return pv_dict

    def complete_dictionary(self, cod_dict):

        new_dictionary = copy.deepcopy(cod_dict)

        for key, variable in new_dictionary.items():

            if 'desc' not in variable:
                variable['desc'] = self.get_question(variable['origin'])

            if 'pv' not in variable:
                variable['pv'] = self.get_pv_dict(variable['origin'])

        return new_dictionary


class PnsDict:

    def __init__(self):
        self.df = pd.read_csv('../data/processed/PNS_2019/dictionary.csv')

        def _convert_str_dict(d):
            return ast.literal_eval(d)

        self.df['pv'] = self.df['pv'].apply(_convert_str_dict)

    def get_df_cod(self, cod):
        return self.df[self.df['index'] == cod]

    def get_question(self, cod):
        try:
            return self.get_df_cod(cod)['desc'].values[0].strip()
        except:
            return ''

    def get_pv_dict(self, cod):
        return self.get_df_cod(cod)['pv'].values[0]


PNS_DICT_RAW = PnsDictRaw()

PNS_DICT = PnsDict()

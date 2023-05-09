import pandas as pd


class PenseDict:

    def __init__(self):
        xls = pd.ExcelFile('../data/raw/PENSE_2019/Dicionario_PENSE2019_Microdados.xls')

        def process(df_i):
            df_i = df_i[2:]
            df_i = df_i.dropna(subset=['desc', 'pv', 'pv_desc'], how='all')
            df_i[['cod', 'desc']] = df_i[['cod', 'desc']].ffill()
            df_i['cod'] = df_i['cod'].str.upper()
            return df_i

        df1 = pd.read_excel(xls, sheet_name='Variáveis cadastrais e amostra', names=['cod', 'desc', 'pv', 'pv_desc'])
        df1 = process(df1)

        df2 = pd.read_excel(xls, sheet_name='Questionário ALUNO', names=['cod', 'desc', 'pv', 'pv_desc'])
        df2 = process(df2)

        df3 = pd.read_excel(xls, sheet_name='Questionário ESCOLA', names=['cod', 'desc', 'pv', 'pv_desc'])
        df3 = process(df3)

        self.df = pd.concat([df1, df2, df3])

    def get_df_cod(self, cod):
        return self.df[self.df['cod'] == cod]

    def get_question(self, cod):
        return self.get_df_cod(cod)['desc'].values[0]

    def get_pv_dict(self, cod):
        dictionary = self.get_df_cod(cod)[['pv', 'pv_desc']].set_index('pv')['pv_desc'].to_dict()
        return {int(k): v for k, v in dictionary.items()}

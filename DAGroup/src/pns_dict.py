import pandas as pd




KEY_HOUSE = ['V0001', 'V0024', 'UPA_PNS', 'V0006_PNS']
KEY_SUBJECT = KEY_HOUSE + ['C00301']
LIFE_STYLES = ['P00102', 'P00103', 'P00104', 'P00201', 'P00402', 'P00403', 'P00404',
               'P00405', 'P005', 'P00601', 'P00602', 'P00603', 'P00604', 'P00605',
               'P00607', 'P00608', 'P00609', 'P00610', 'P00611', 'P00612', 'P00613',
               'P00614', 'P00615', 'P00616', 'P00617', 'P00618', 'P00619', 'P00620',
               'P00621', 'P00622', 'P00623', 'P006', 'P00901', 'P01001', 'P01101',
               'P013', 'P015', 'P02001', 'P02101', 'P01601', 'P018', 'P019',
               'P02002', 'P02102', 'P023', 'P02401', 'P02501', 'P02602',
               'P02601', 'P027', 'P02801', 'P029', 'P03201', 'P03202', 'P03001',
               'P03301', 'P03302', 'P03303', 'P034', 'P035', 'P03701', 'P03702',
               'P036', 'P038', 'P039', 'P03904', 'P03905', 'P03906', 'P040',
               'P04001', 'P04101', 'P04102', 'P042', 'P04301', 'P04302',
               'P044', 'P04401', 'P04405', 'P04406', 'P04501', 'P04502', 'P046',
               'P04701', 'P04801', 'P04902', 'P050', 'P051', 'P052', 'P053',
               'P05401', 'P05402', 'P05403', 'P05404', 'P05405', 'P05406', 'P05407',
               'P05408', 'P05409', 'P05410', 'P05411', 'P05412', 'P05413', 'P05414',
               'P05415', 'P05416', 'P05417', 'P05418', 'P05419', 'P05421', 'P05422',
               'P055', 'P056', 'P05601', 'P05602', 'P05603', 'P05604', 'P05605',
               'P057', 'P058', 'P05801', 'P05802', 'P05901', 'P05902', 'P05903', 'P05904',
               'P05905', 'P05906', 'P060', 'P06101', 'P06102', 'P06103', 'P06104',
               'P06105', 'P06106', 'P06302', 'P067', 'P06701', 'P068', 'P069', 'P06901',
               'P07004', 'P07005', 'P07006', 'P07007', 'P07101', 'P07201']

DEPRESSION_REF = ['Q092']


class PnsDict:

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
        return self.get_df_cod(cod)['desc'].values[0]

    def get_pv_dict(self, cod):
        dictionary = self.get_df_cod(cod)[['pv', 'pv_desc']].set_index('pv')['pv_desc'].to_dict()
        return {int(k): v for k, v in dictionary.items()}


PNS_DICT = PnsDict()

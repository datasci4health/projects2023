import pandas as pd
import geopandas as gpd
from pense_dict import PenseDict

BRAZIL_MAP_GPD = gpd.read_file('../assets/brazil-states.geojson')
BRAZIL_MAP_GPD['codigo_ibg'] = BRAZIL_MAP_GPD['codigo_ibg'].astype(int)

BRAZIL_IDH = pd.read_csv('../data/raw/PENSE_2019/IDH_2019.csv', delimiter=';', decimal=",")
BRAZIL_IDH = BRAZIL_MAP_GPD[['name', 'codigo_ibg']].merge(BRAZIL_IDH, left_on='name', right_on='Territorialidade')
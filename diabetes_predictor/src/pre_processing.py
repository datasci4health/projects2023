import pandas as pd

df = pd.read_excel('Vigitel-2019-peso-rake.xls', sheet_name='Sheet1')

df_input = pd.DataFrame()
df_input["peso"] = df.loc[(df.q9 > 0) & (df.q9 < 150), "q9"].reset_index(drop=True)
df_input["altura"] = df.loc[(df.q11 > 0) & (df.q11 < 250), "q11"].reset_index(drop=True)
df_input["exercicio_fisico"] = df["q42"]
df_input["diabetes"] = (df["q76"] == 1).astype(int)  # convert boolean to integer
df_input["idade"] = df.loc[(df.q6 > 0) & (df.q6 < 120), "q6"].reset_index(drop=True)
df_input = df_input.dropna().reset_index(drop=True)
print(df_input.shape)
df_input.to_csv("output_cluster.csv")
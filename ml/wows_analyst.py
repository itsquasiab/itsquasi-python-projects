import pandas as pd

file_path = 'ml/input/wows_ship_stats.csv'

df = pd.read_csv(file_path)

#print(df.info())
#print(df.groupby("Nation")["Players"].sum())
#print(df.groupby("Tier")["Players"].sum())
print(df.groupby("Ship")["Players"].max())
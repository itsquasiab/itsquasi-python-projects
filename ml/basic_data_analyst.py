import pandas as pd

file_path = 'ml/input/wows_ship_stats.csv'

df = pd.read_csv(file_path)
#print(df.Ship)
#print(df['Ship'])
#print(df['Ship'][0])
print(df[['Ship', 'Tier', 'Nation']])
#for i in df['Ship']: print(i)
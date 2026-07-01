import pandas as pd

file_path = 'ml/input/wows_ship_stats.csv'

df = pd.read_csv(file_path)
#print(df.Ship)
#print(df['Ship'])
#print(df['Ship'][0])
#print(df[['Ship', 'Tier', 'Nation']])
#print(df['Nation'] == 'U.S.A.')
#print(df.notnull().sum())
#for i in df['Ship']: print(i)
print(df.head(20))
print(df.tail(20))
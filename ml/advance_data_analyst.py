import pandas as pd

file_path = 'ml/input/wows_ship_stats.csv'

df = pd.read_csv(file_path)
desc = df.describe()

for col in ['Win rate', 'Survival rate']:
    desc[col] = desc[col].map(lambda x: f'{x:.1%}')

for col in ['Tier', 'Players', 'Battles', 'Base XP', 'Damage', 'Frags', 'Capture', 'Defence', 'Spotting', 'Potential', 'Aircraft']:
    desc[col] = desc[col].map(lambda x: f'{x:,.0f}')

print(desc)
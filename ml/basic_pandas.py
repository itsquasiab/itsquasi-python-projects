import pandas as pd

data = {
    'Bob': ['I liked it.', 'It was awful.', 'So so.'], 
    'Sue': ['Pretty good.', 'Bland.', 'Fantastic!']
}

df = pd.DataFrame(data, index=['Product A', 'Product B', 'Product C'])
sr = pd.Series([1, 2, 3, 4, 5])

print(df)
print(df.loc['Product A'])
print(df.loc['Product A', 'Bob'])
print(df.loc['Product A':'Product B', 'Bob'])
#print(sr)
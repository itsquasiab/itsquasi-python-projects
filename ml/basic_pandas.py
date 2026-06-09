import pandas as pd

data = {
    'Bob': ['I liked it.', 'It was awful.'], 
    'Sue': ['Pretty good.', 'Bland.']
}
series = [1, 2, 3, 4, 5]

display_data = pd.DataFrame(data, index=['Product A', 'Product B'])
display_series = pd.Series(series)

print(display_data)
print(display_series)
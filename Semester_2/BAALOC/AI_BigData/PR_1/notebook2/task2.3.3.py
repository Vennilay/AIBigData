import pandas as pd

f = pd.read_csv('diamonds.csv')
print(f.head(5))
print()
print(f.tail(5))
print()
print(f.shape)
print(f.describe())
print()
print(f.iloc[1:5])
print()
f = f[f['color'] == 'E']
print(f)

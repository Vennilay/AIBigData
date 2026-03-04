import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
df = pd.read_csv (url)

df.head(2)
df.tail(3)
df.shape
df.describe()
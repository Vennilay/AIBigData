import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
df = pd.read_csv (url)

df.iloc[1:4]

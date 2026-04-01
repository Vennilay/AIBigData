import pandas as pd

url = 'https://raw.githubusercontent.com/akmand/datasets/main/abolone.csv'
df = pd.read_csv(url)

print(df.head())
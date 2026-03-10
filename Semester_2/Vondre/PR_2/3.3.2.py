import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

url = 'https://raw.githubusercontent.com/akmand/datasets/master/iris.csv'
df = pd.read_csv(url)

minmax_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

df['sepal_length_cm'] = minmax_scaler.fit_transform(df[['sepal_length_cm']])

df['sepal_width_cm'] = standard_scaler.fit_transform(df[['sepal_width_cm']])

print(df.head())
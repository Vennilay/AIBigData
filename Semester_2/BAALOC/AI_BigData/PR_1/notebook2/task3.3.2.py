import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = pd.read_csv('iris.csv')
minimax_scaler = MinMaxScaler()
standard_scaler = StandardScaler()

minimax_res = minimax_scaler.fit_transform(data[['sepal_length_cm']])
standard_res = standard_scaler.fit_transform(data[['sepal_width_cm']])

print(minimax_res[:5])
print()
print(standard_res[:5])

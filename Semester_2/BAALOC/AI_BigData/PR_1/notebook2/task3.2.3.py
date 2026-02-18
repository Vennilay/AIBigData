import pandas as pd
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
dfTest = pd.DataFrame({'A': [14.00, 19.00],
                       'B': [103.02, 107.26],
                       'C': ['big', 'small']})

dfTest[['A', 'B']] = scaler.fit_transform(dfTest[['A', 'B']])
print(dfTest)

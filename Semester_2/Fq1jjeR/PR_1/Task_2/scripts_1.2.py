
'''
№1.2.1
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
print(x)
print(x[3][1])
print(x[1])

№1.2.2

import numpy as np

a = np.zeros(10)
b = np.ones(10)
c = np.full(10, 5)
d = np.arange(10, 20)
print(a, "\n", b, "\n", c, "\n", d)


№1.2.3

import numpy as np

Z = np.random.random((10, 10))
Zmin, Zmax, Zmean = Z.min(), Z.max(), Z.mean()
print(Zmin, Zmax, Zmean)

№1.2.4

import numpy as np

A = np.arange(25).reshape(5, 5)
A[[0, 1]] = A[[1, 0]]
print(A)

№1.2.5

import numpy as np

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)

№1.2.6

import numpy as np

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print(np.sort(arr))

№1.3.1

import numpy as np
A = np.zeros((8, 8), dtype='int32')
A[1::2, ::2] = 1
A[::2, 1::2] = 1
print(A)

№1.3.2

import numpy as np
row = np.arange(5)
A = np.zeros((5, 5), dtype='int32') + row
print(A)

№1.3.3

import numpy as np
A = np.random.random((3, 3, 3))
print(A)

№1.3.4
import numpy as np
A = np.ones((5, 5), dtype='int32')
A[1:-1, 1:-1] = 0
print(A)

№1.3.5
import numpy as np
A = np.array([5, 2, 9, 1, 7])
A = np.sort(A)[::-1]
print(A)

№1.3.6

import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A)
print(A.shape)
print(A.size)
print(A.ndim)

№2.2.1

import pandas as pd

lst = [1, 2, 3, 4, 5]
d = {'a': 1, 'b': 2, 'c': 3}

ndarr = pd.array([1, 2, 3, 4, 5])

s1 = pd.Series(lst)
s2 = pd.Series(d)
s3 = pd.Series(ndarr, ['a', 'b', 'c', 'd', 'e'])

print(s1)
print(s2)
print(s3)

№2.2.2

import pandas as pd

s1 = pd.Series([1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series([5, 4, 3, 2, 1])

print(s1['a'])
print(s2[0])
print(s2[3:])


№2.2.3

import pandas as pd

dataframe = pd.DataFrame()
dataframe['Имя'] = ['Джеки Дженсон', 'Стивен Стивенсон']
dataframe['Возраст'] = [38, 25]
dataframe['Водитель'] = [True, False]

print(dataframe)

№2.2.4
import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
dataframe = pd.read_csv(url)
print(dataframe.head(5))

№2.2.5

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
dataframe = pd.read_csv(url)
print(dataframe.head(2))
print(dataframe.tail(3))
print(dataframe.shape)
print(dataframe.describe())

№2.2.6

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
dataframe = pd.read_csv(url)
print(dataframe.iloc[1:4])

№2.2.7

import pandas as pd

url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
dataframe = pd.read_csv(url)
print(dataframe[dataframe['PClass'] == '1st'].head(2))

№2.3.1

import pandas as pd
a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])
dist = ((a - b)**2).sum()**0.5
print(dist)

№2.3.2

import pandas as pd
a = pd.read_csv('cdc.csv')
print(a.head(5))

№2.3.3

import pandas as pd
a = pd.read_csv('cdc.csv')
print(a.head(5))
print()
print(a.tail(5))
print()
print(a.shape)
print(a.describe())
print()
print(a.iloc[25:35])
print()
a = a[a['genhlth'] == 'excellent']
print(a)

№3.2.1

import numpy as np
from sklearn import preprocessing

feature = np.array([[-500.5], [-100.1], [0], [100.1], [900.9]])
minimax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
scaled_feature = minimax_scale.fit_transform(feature)

print(scaled_feature)


№3.2.2
import numpy as np
from sklearn import preprocessing

x = np.array([[-1000.1], [-200.2], [500.5], [600.6], [9000.0]])

scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(x)

print(standardized)

№3.2.3

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
dfTest = pd.DataFrame({'A': [14.00, 19.00],
                       'B': [103.02, 107.26],
                       'C': ['big', 'small']})

dfTest[['A', 'B']] = scaler.fit_transform(dfTest[['A', 'B']])
print(dfTest)

№3.3.2

import pandas as pd
a = pd.read_csv(r'C:\Users\nikit\PyCharmMiscProject\iris.csv')
a['sepal_length_cm'] = (a['sepal_length_cm'] - a['sepal_length_cm'].min()) / (a['sepal_length_cm'].max() - a['sepal_length_cm'].min())
a['sepal_width_cm'] = (a['sepal_width_cm'] - a['sepal_width_cm'].mean()) / a['sepal_width_cm'].std(ddof=0)
print(a[['sepal_length_cm', 'sepal_width_cm']].head(5))
'''

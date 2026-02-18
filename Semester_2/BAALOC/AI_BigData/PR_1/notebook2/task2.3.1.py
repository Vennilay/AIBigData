import numpy as np
import pandas as pd

d1 = pd.Series([0, 0], ['x', 'y'])
d2 = pd.Series([3, 4], ['x', 'y'])
res = np.sqrt(np.abs(d1['x'] - d2['x']) ** 2 + np.abs(d1['y'] - d2['y']) ** 2)
print(res)

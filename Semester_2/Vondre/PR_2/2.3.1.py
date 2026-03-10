import pandas as pd
import math

a = pd.Series([1, 2, 3])
b = pd.Series([4, 6, 8])

distance = math.sqrt(((a - b) ** 2).sum())

print(distance)
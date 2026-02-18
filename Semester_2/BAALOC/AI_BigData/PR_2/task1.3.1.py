import numpy as np

i, j = np.indices((5, 5))
x = (i + j) % 2
print(x)

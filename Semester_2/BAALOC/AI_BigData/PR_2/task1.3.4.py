import numpy as np

x = np.zeros((5, 5), dtype=int)
x[0, :] = 1
x[:, 0] = 1
x[:, 4] = 1
x[4, :] = 1
print(x)

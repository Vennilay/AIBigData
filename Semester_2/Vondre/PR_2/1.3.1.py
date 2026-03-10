import numpy as np

a = np.arange(64).reshape(8,8)
for i in range(8):
    for j in range(8):
        a[i][j] = (i+j)%2
print(a)
import numpy as np

n = 8
a = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            a[i,j] = 1
        if j == 0 or j == n-1:
            a[i,j] = 1
print(a)
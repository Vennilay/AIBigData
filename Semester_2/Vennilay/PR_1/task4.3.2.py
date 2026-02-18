import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11, 1)

f1 = np.sqrt(1 + np.e ** np.sqrt(x) + np.cos(x ** 2))
f2 = np.abs(1 - np.sin(x) ** 3)
f3 = np.log(np.abs(2 * x))
y = f1 / f2 + f3

plt.grid()
plt.plot(x, y, c='b')

plt.scatter(x[:len(x) // 2], y[:len(x) // 2], c='b')
plt.plot(x[:len(x) // 2], y[:len(x) // 2])
plt.show()




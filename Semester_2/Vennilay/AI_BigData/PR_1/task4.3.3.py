import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 11, 1)
y = np.abs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1))))

area = np.trapezoid(y, x)
plt.grid()
plt.plot(x, y, c='r')
plt.fill_between(x, y, color='b')
plt.show()

print(area)

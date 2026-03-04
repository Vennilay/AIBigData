import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,1)
y = np.abs(np.cos(x * np.e ** (np.cos(x) + np.log(x + 1))))


plt.grid(True)
plt.plot(x, y, color='red')
plt.fill_between(x, y)
plt.show()

area = np.trapezoid(y)
print(area)
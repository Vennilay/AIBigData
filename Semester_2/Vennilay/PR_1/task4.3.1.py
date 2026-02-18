import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(100)

print("mean", x.mean())
print("median", np.median(x))

plt.scatter(range(len(x)), x)
plt.show()

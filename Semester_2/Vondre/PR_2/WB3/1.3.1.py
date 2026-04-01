import numpy as np
import matplotlib.pyplot as plt

p1 = np.array([0, 0, 0])
p2 = np.array([3, 3, 3])
p3 = np.array([1, 3, 2])
p4 = np.array([3, 0, 1])
dots = np.array([p1, p2, p3, p4])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(dots[:, 0], dots[:, 1], dots[:, 2], color='red')
plt.show()

print(np.linalg.norm(p1 - p2))
print(np.linalg.norm(p1 - p3) ** 2)
print(np.linalg.norm(p1 - p4, ord=np.inf))
print(np.linalg.norm(p2 - p1, ord=1))



import matplotlib.pyplot as plt
import numpy as np

p1 = np.array([1, 2, 3])
p2 = np.array([4, -1, 2])
p3 = np.array([0, 5, -2])
p4 = np.array([-3, 2, 7])
dots = np.array([p1, p2, p3, p4])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(dots[:, 0], dots[:, 1], dots[:, 2], color='blue', s=50)

plt.show()

print(np.linalg.norm(p1 - p2))
print(np.linalg.norm(p1 - p3) ** 2)
print(np.linalg.norm(p1 - p4, ord=np.inf))
print(np.linalg.norm(p2 - p1, ord=1))

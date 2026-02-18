from random import randint

import matplotlib.pyplot as plt

x = list([randint(1, 99) / 100 for _ in range(100)])
i = list(range(100))
average = sum(x) / len(x)

median = (sorted(x)[len(x) // 2 - 1] + sorted(x)[len(x) // 2]) / 2
print("Average: ", average)
print("Median: ", median)

fig = plt.figure(figsize=(10, 7))
plt.scatter(i, x)
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.grid()
plt.show()

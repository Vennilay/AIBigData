import math
import matplotlib.pyplot as plt

n=10
data = []
for x in range(1,n+1):
    data.append((math.sqrt(1 + math.e ** math.sqrt(x) + math.cos(x) ** 2)) / abs(1 - math.sin(x) ** 3))
print(data)

dataHalf = data[:n//2]
print(dataHalf)


plt.title("Основной массив")
plt.grid()
plt.plot(data)
plt.show()

plt.title("Срез")
plt.grid()
xHalf = list(range(n//2))
plt.scatter(xHalf, dataHalf)

plt.show()
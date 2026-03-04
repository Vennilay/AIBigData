from  random import random

import matplotlib.pyplot as plt

data = []
unsortedData = []
n = 20
srZnach=0
mediana = 0
biggest = ''
smallest = ''

for i in range(n):
    data.append(random())
    unsortedData.append(random())
for i in data:
    srZnach+=i
srZnach/= n
print(srZnach)

data.sort()
if n%2==0:
    mediana = (data[n // 2] + data[n // 2 - 1]) / 2
else:
    mediana = data[n // 2]
print(mediana)
biggest= "Медиана" if mediana>srZnach else "Среднее значение"
smallest= "медиана" if mediana<srZnach else "среднее значение"
print(biggest + " больше чем " + smallest)

x = list(range(1, n + 1))

plt.grid(True)
plt.scatter(x, unsortedData)
plt.show()
'''
№1.2
x = 3 + 5.2 * 7
y = None
z = 'a', 5, 12.345, (2, 'b')
df = [['Антонова Антонина', 34, 'ж'], ['Борисов Борис', 26, 'м']]
A = {1, 'title', 2, 'content'}
print(x, '|', type(x), '\n', y, '|', type(y), '\n',
      z, '|', type(z), '\n', df, '|', type(df), '\n', A, '|', type(A) )


№1.3
x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонина Антонина', 34, 'ж'
z = 'type'
D = [1, 'title', 2, 'content']
print(x, '|', type(x), '\n', A, '|', type(A), '\n',
      B, '|', type(B), '\n', C, '|', type(C), '\n',
      df, '|', type(df), '\n', z, '|', type(z), '\n',
      D, '|', type(D))

№2.2
x = 125
if x < 0:
    print("x отрицательный")
elif x == 0:
    print("x равен нулю")
else:
    print("x положительный")

№2.3
    x = int(input())
if x < -5:
    print('x принадлежит (-inf, 5)')
elif -5 <= x <= 5:
    print('x принадлежит [-5, 5]')
else:
    print('x принадлежит (5, +inf)')

№3.2.1x`x
x = 1
while x <= 10:
    print(x)
    x += 3

№3.2.2

models = ['KNN', 'decision tree', 'linear model']
for model in models:
    print(model)

№3.2.3
list int = range(1, 100, 7)
print(list(list_int))

№3.2.4
for i in range(5, 106, 25):
    print(i)

№3.2.5
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[1:7:2]
c = a[::-1]
print(b)
print(c)

№3.3.1

_list = []
x = 1
while x <= 10:
    _list.append(x)
    x +=3

print(*_list[::-1], sep='\n')

№3.3.2

_list = ["age", "gender", "height", "education", "income"]
for i in _list:
    print(i)

№3.3.3

_list = [int(i) for i in range(2, 16, 1)]
print(_list)

№3.3.4
for i in range(105, 4, -25):
    print(i)

№3.3.5

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x[::2] = x[::2][::-1]
print(x)

№4.2.1
import math as m
print(m.sin (m.e))

№4.2.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from numpy import trapezoid
x = np.arange(0.0, 10, 0.1)
y = np.abs(np.sin(x*np.exp(np.cos(x))))
plt.grid()
plt.plot(x, y, c = "r")
plt.fill_between(x, y)

area = trapezoid(y)
print (area)
plt.show()


№4.2.3

from matplotlib import pyplot as plt
import numpy as np

marks = ['Неуд', 'Удовл', 'Хор', 'Отл']
data = [3, 7, 8, 4]

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=marks)

plt.show()
plt.grid()
plt.scatter(marks, data)
plt.show()

№4.3.1
import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(250)

print(f"Среднее: {np.mean(data):.3f}")
print(f"Медиана: {np.median(data):.3f}")

plt.scatter(range(len(data)), data)
plt.show()

№4.3.2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 10)
y = (np.sqrt(1 + np.exp(np.sqrt(x)) + np.cos(x**2)) /
     np.abs(1 - np.sin(x)**3)) + np.log(np.abs(2*x))

x_slice = x[:5]
y_slice = y[:5]

plt.plot(x, y, label='Main')
plt.scatter(x_slice, y_slice, color='red', label='Slice')
plt.legend()
plt.grid(True)
plt.show()

№4.3.3
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapezoid

x = np.arange(0, 11, 1)
y = np.abs(np.cos(x * np.exp(np.cos(x) + np.log(x + 1))))

area = trapezoid(y, x)
print(f"Площадь под графиком: {area:.3f}")

plt.plot(x, y)
plt.fill_between(x, y, color='blue', alpha=0.3)
plt.grid(True)
plt.show()

№4.3.4
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, start="2021-01-01", end="2022-01-01")['Close']

normalized_data = data / data.iloc[0]
normalized_data.plot(figsize=(10, 6))

plt.title('Динамика акций Apple, Microsoft и Google за 2021 год')
plt.ylabel('Относительное изменение')
plt.xlabel('Дата')
plt.grid(True)
plt.legend(tickers)
plt.show()

№4.3.5
import math
x = float(input("Введите x: "))
y = float(input("Введите y: "))

print(f"Сумма: {x + y}")
print(f"Разность: {x - y}")
print(f"Произведение: {x * y}")
print(f"Частное: {x / y if y != 0 else 'ошибка (деление на 0)'}")

print(f"e^(x+y): {math.exp(x + y)}")
print(f"sin(x+y): {math.sin(x + y)}")
print(f"cos(x+y): {math.cos(x + y)}")
print(f"x^y: {pow(x, y)}")

'''
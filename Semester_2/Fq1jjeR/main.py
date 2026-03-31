import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

x = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
y = np.array([5.0, 5.0, 4.0, 4.0, 6.0, 6.0])

z1 = np.polyfit(x, y, 1)
p1 = np.poly1d(z1)
print("Коэффициенты полинома 1-й степени (a, b):")
print(z1)

z2 = np.polyfit(x, y, 2)
p2 = np.poly1d(z2)
print("\nКоэффициенты полинома 2-й степени (a, b, c):")
print(z2)

sko1 = np.sqrt(mean_squared_error(y, p1(x)))
sko2 = np.sqrt(mean_squared_error(y, p2(x)))

print(f"\nСКО для 1-й степени: {sko1}")
print(f"СКО для 2-й степени: {sko2}")

plt.scatter(x, y, color='gray', label='Данные')
x_highres = np.linspace(3, 4, 100)

plt.plot(x_highres, p1(x_highres), color='red', label='1-я степень')
plt.plot(x_highres, p2(x_highres), color='green', label='2-я степень')

plt.title('Аппроксимация (Вариант 2)')
plt.legend()
plt.show()
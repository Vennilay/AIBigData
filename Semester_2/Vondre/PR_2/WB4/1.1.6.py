import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

xdata = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float)
ydata = np.array([2.1, 4.5, 7.9, 12.8, 18.9, 26.7, 35.8, 46.2], dtype=float)

def f_log(x, b0, b1):
    return b0 + b1 * np.log(x)

def f_pow(x, b0, b1):
    return b0 * x ** b1

beta_log, cov_log = sp.optimize.curve_fit(f_log, xdata, ydata)
beta_pow, cov_pow = sp.optimize.curve_fit(f_pow, xdata, ydata)

print("Коэффициенты логарифмической модели:", beta_log)
print("Коэффициенты степенной модели:", beta_pow)

y_log = f_log(xdata, *beta_log)
y_pow = f_pow(xdata, *beta_pow)

lin_dev_log = np.sum(cov_log[0])
lin_dev_pow = np.sum(cov_pow[0])

print("Линейное отклонение (log):", lin_dev_log)
print("Линейное отклонение (pow):", lin_dev_pow)

rss_log = np.sum((ydata - y_log) ** 2)
rss_pow = np.sum((ydata - y_pow) ** 2)

print("Квадратичное отклонение RSS (log):", rss_log)
print("Квадратичное отклонение RSS (pow):", rss_pow)

plt.figure(figsize=(10, 6))
plt.scatter(xdata, ydata, label="Собственные данные")
plt.plot(xdata, y_log, 'r-', lw=2, label="Логарифмическая модель")
plt.plot(xdata, y_pow, 'g-', lw=2, label="Степенная модель")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Сравнение аппроксимации данных")
plt.legend()
plt.grid(True)
plt.show()
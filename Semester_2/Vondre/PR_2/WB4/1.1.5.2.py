import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

xdata = np.linspace(1, 10, 20)
ydata = np.array([2.3, 3.8, 4.1, 5.7, 6.1, 7.5, 8.2, 9.5, 9.9, 11.2,
                  12.1, 13.5, 14.2, 14.8, 16.5, 17.2, 18.0, 18.9, 19.5, 20.8])


def f1(x, b0, b1):
    return b0 + b1 * x


def f2(x, b0, b1, b2):
    return b0 + b1 * x + b2 * x ** 2


def f3(x, b0, b1):
    return b0 + b1 * np.log(x)


def f4(x, b0, b1):
    return b0 * x ** b1


beta_opt1, _ = curve_fit(f1, xdata, ydata)
beta_opt2, _ = curve_fit(f2, xdata, ydata)
beta_opt3, _ = curve_fit(f3, xdata, ydata)
beta_opt4, _ = curve_fit(f4, xdata, ydata)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

ax1.scatter(xdata, ydata, c='k', label='Данные')
ax1.plot(xdata, f1(xdata, *beta_opt1), 'b', lw=2, label='Линейная')
ax1.set_title('Линейная модель')
ax1.legend()

ax2.scatter(xdata, ydata, c='k', label='Данные')
ax2.plot(xdata, f2(xdata, *beta_opt2), 'r', lw=2, label='Квадратичная')
ax2.set_title('Квадратичная модель')
ax2.legend()

ax3.scatter(xdata, ydata, c='k', label='Данные')
ax3.plot(xdata, f3(xdata, *beta_opt3), 'g', lw=2, label='Логарифмическая')
ax3.set_title('Логарифмическая модель')
ax3.legend()

ax4.scatter(xdata, ydata, c='k', label='Данные')
ax4.plot(xdata, f4(xdata, *beta_opt4), 'm', lw=2, label='Степенная')
ax4.set_title('Степенная модель')
ax4.legend()

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Вариант 5
x = np.array([5.0, 5.2, 5.4, 5.6, 5.8, 6.0])
y = np.array([2.0, 4.0, 4.0, 3.0, 3.0, 3.0])

A1 = np.vstack((x, np.ones(len(x)))).T
a1, b1 = np.linalg.lstsq(A1, y, rcond=None)[0]

y_pred1 = a1 * x + b1
sko1 = np.sqrt(np.mean((y - y_pred1) ** 2))

print(f"Уравнение: y = {a1:.4f}x + {b1:.4f}")
print(f"СКО: {sko1:.4f}\n")

A2 = np.vstack((x ** 2, x, np.ones(len(x)))).T
a2, b2, c2 = np.linalg.lstsq(A2, y, rcond=None)[0]

y_pred2 = a2 * x ** 2 + b2 * x + c2
sko2 = np.sqrt(np.mean((y - y_pred2) ** 2))

print(f"Уравнение: y = {a2:.4f}x^2 + {b2:.4f}x + {c2:.4f}")
print(f"СКО: {sko2:.4f}")

x_plot = np.linspace(min(x) - 0.1, max(x) + 0.1, 100)
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ko', markersize=8, label='Исходные данные')
plt.plot(x_plot, a1 * x_plot + b1, 'b-', lw=2, label=f'1-я степень (СКО={sko1:.2f})')
plt.plot(x_plot, a2 * x_plot ** 2 + b2 * x_plot + c2, 'r-', lw=2, label=f'2-я степень (СКО={sko2:.2f})')
plt.title('Аппроксимация методом наименьших квадратов')
plt.legend()
plt.grid()
plt.show()

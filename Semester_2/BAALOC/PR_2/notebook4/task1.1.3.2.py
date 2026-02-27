import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([2.1, 3.5, 4.2, 5.8, 8.1, 11.5, 14.2])

x_prec = np.linspace(1, 10, 100)

m1 = np.vstack((x, np.ones(len(x)))).T
s1 = np.linalg.lstsq(m1, y, rcond=None)[0]
y_prec1 = s1[0] * x_prec + s1[1]

m2 = np.vstack((x ** 2, x, np.ones(len(x)))).T
s2 = np.linalg.lstsq(m2, y, rcond=None)[0]
y_prec2 = s2[0] * x_prec ** 2 + s2[1] * x_prec + s2[2]

m3 = np.vstack((x ** 3, x ** 2, x, np.ones(len(x)))).T
s3 = np.linalg.lstsq(m3, y, rcond=None)[0]
y_prec3 = s3[0] * x_prec ** 3 + s3[1] * x_prec ** 2 + s3[2] * x_prec + s3[3]

plt.figure(figsize=(10, 6))

plt.plot(x, y, 'ko', markersize=8, label='Исходные данные')

plt.plot(x_prec, y_prec1, 'r-', lw=2, label='1-я степень (Прямая)')
plt.plot(x_prec, y_prec2, 'b-', lw=2, label='2-я степень (Парабола)')
plt.plot(x_prec, y_prec3, 'g-', lw=2, label='3-я степень (Куб)')

plt.xlabel('Месяцы')
plt.ylabel('Продажи')
plt.legend()
plt.grid()
plt.show()

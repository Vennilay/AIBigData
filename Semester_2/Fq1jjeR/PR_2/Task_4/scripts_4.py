'''
#1.1.1 Пример
import numpy as np
import matplotlib.pyplot as plt

# 1. Подготовка данных
x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])

A = np.vstack([x, np.ones(len(x))]).T
print(A)
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(f"m = {m}, c = {c}")

plt.plot(x, y, 'o', label='Исходные данные', markersize=10)
plt.plot(x, m*x + c, 'r', label='Линейная экстраполяция')
plt.legend()
plt.show()

#1.1.2 Пример
from numpy import *
from numpy.random import *
import matplotlib.pyplot as plt

delta = 1.0
x = linspace(-5, 5, 11)
y = x**2 + delta * (rand(11) - 0.5)
x += delta * (rand(11) - 0.5)

x.tofile('x_data.txt', sep='\n')
y.tofile('y_data.txt', sep='\n')


x_read = fromfile('x_data.txt', float, sep='\n')
y_read = fromfile('y_data.txt', float, sep='\n')

print("Массив X:", x_read)
print("Массив Y:", y_read)

m = vstack((x_read**2, x_read, ones(len(x_read)))).T

s = linalg.lstsq(m, y_read, rcond=None)[0]

x_prec = linspace(-5, 5, 101)

plt.plot(x_read, y_read, 'D', label='Точки с шумом')

plt.plot(x_prec, s[0] * x_prec**2 + s[1] * x_prec + s[2], '-', lw=2, label='Итоговая парабола')

plt.grid()
plt.legend()
plt.savefig('парабола.png')
plt.show()

#1.1.3 Пример
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 11)
y = x**3 + np.random.randn(11) * 5

m = np.vstack((x**3, x**2, x, np.ones(11))).T

s = np.linalg.lstsq(m, y, rcond=None)[0]

x_prec = np.linspace(-5, 5, 101)

plt.plot(x, y, 'D')

plt.plot(x_prec, s[0] * x_prec**3 + s[1] * x_prec**2 + s[2] * x_prec + s[3], '-', lw=3)

plt.grid()
plt.savefig('полином 3-й степени.png')
plt.show()

# 1.1.3 Задание
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 12)
y = x**3 - 10*x**2 + 3*x + 500 + np.random.randn(12) * 50

m1 = np.vstack((x, np.ones(len(x)))).T
s1 = np.linalg.lstsq(m1, y, rcond=None)[0]

m2 = np.vstack((x**2, x, np.ones(len(x)))).T
s2 = np.linalg.lstsq(m2, y, rcond=None)[0]

m3 = np.vstack((x**3, x**2, x, np.ones(len(x)))).T
s3 = np.linalg.lstsq(m3, y, rcond=None)[0]

x_prec = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'D', label='Мои данные', color='black')

plt.plot(x_prec, s1[0]*x_prec + s1[1], '--', label='1-я степень (линейная)')
plt.plot(x_prec, s2[0]*x_prec**2 + s2[1]*x_prec + s2[2], '-', label='2-я степень (квадратичная)')
plt.plot(x_prec, s3[0]*x_prec**3 + s3[1]*x_prec**2 + s3[2]*x_prec + s3[3], '-', lw=3, label='3-я степень (кубическая)')

plt.legend()
plt.grid(True)
plt.title("Экстраполяция полиномами разных степеней")
plt.show()

#1.1.4 Пример
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(x, b0, b1, b2):
    return b0 + b1 * np.exp(-b2 * x**2)

beta = (0.25, 0.75, 0.5)
xdata = np.linspace(0, 5, 50)
y = f(xdata, *beta)

ydata = y + 0.05 * np.random.randn(len(xdata))

print("Массив xdata:")
print(xdata)
print("\nМассив ydata:")
print(ydata)

beta_opt, beta_cov = curve_fit(f, xdata, ydata)
print(beta_opt)
lin_dev = sum(np.diag(beta_cov))
print(f"\nЛинейное отклонение: {lin_dev}")

residuals = ydata - f(xdata, *beta_opt)
fres = sum(residuals**2)
print(f"Квадратичное отклонение: {fres}")

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(xdata, ydata, label='Данные с шумом')

ax.plot(xdata, y, 'r', lw=2, label='Исходная функция')

ax.plot(xdata, f(xdata, *beta_opt), 'b', lw=2, label='Подобранная модель')

ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
ax.legend()
plt.grid(True)
plt.show()

# 1.1.5 Пример
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

xdata = np.linspace(1, 5, 50)


def print_and_plot(title, x, y_noisy, func, beta_init):
    beta_opt, beta_cov = curve_fit(func, x, y_noisy)

    lin_dev = sum(np.diag(beta_cov))
    residuals = y_noisy - func(x, *beta_opt)
    fres = sum(residuals ** 2)

    print(f"\n--- {title} ---")
    print(beta_opt)
    print(lin_dev)
    print(fres)

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y_noisy, s=10, color='blue')
    plt.plot(x, func(x, *beta_opt), color='blue', lw=2)
    plt.xlabel('x')
    plt.ylabel('f(x, beta)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def f1(x, b0, b1): return b0 + b1 * x


y1 = f1(xdata, 0.25, 0.75) + 0.05 * np.random.randn(50)
print_and_plot("Линейная модель", xdata, y1, f1, (0.25, 0.75))


def f2(x, b0, b1, b2): return b0 + b1 * x + b2 * x ** 2


y2 = f2(xdata, 0.25, 0.75, 0.5) + 0.05 * np.random.randn(50)
print_and_plot("Квадратичная модель", xdata, y2, f2, (0.25, 0.75, 0.5))


def f3(x, b0, b1): return b0 + b1 * np.log(x)


y3 = f3(xdata, 1.0, 2.0) + 0.05 * np.random.randn(50)
print_and_plot("Логарифмическая модель", xdata, y3, f3, (1.0, 2.0))


def f4(x, b0, b1): return b0 * x ** b1


y4 = f4(xdata, 1.0, 2.0) + 0.05 * np.random.randn(50)
print_and_plot("Степенная модель", xdata, y4, f4, (1.0, 2.0))



# 1.1.5 Задание
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_own = np.linspace(1, 6, 40)


def print_and_plot(title, x, y_noisy, func, beta_init):
    beta_opt, beta_cov = curve_fit(func, x, y_noisy)

    lin_dev = sum(np.diag(beta_cov))
    residuals = y_noisy - func(x, *beta_opt)
    fres = sum(residuals ** 2)

    print(f"\n--- {title} ---")
    print(beta_opt)
    print(lin_dev)
    print(fres)

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y_noisy, s=10, color='blue')
    plt.plot(x, func(x, *beta_opt), color='red', lw=2)
    plt.xlabel('x')
    plt.ylabel('f(x, beta)')
    plt.title("Собственный эксперимент")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def f_log(x, b0, b1): return b0 + b1 * np.log(x)


y_log = f_log(x_own, 1.5, 2.5) + 0.1 * np.random.randn(40)
print_and_plot("Логарифм", x_own, y_log, f_log, (1.5, 2.5))

def f_pow(x, b0, b1): return b0 * x ** b1

y_pow = f_pow(x_own, 1.2, 1.8) + 0.5 * np.random.randn(40)
print_and_plot("Степенная", x_own, y_pow, f_pow, (1.2, 1.8))


#1.2.1 Пример
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

my_dict = {
    "Учебное время": [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50,
                      2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50],
    "Оценка": [10, 22, 13, 43, 20, 22, 33, 50, 62, 48, 55, 75, 62, 73, 81, 76, 64, 82, 90, 93]
}

dataset = pd.DataFrame(my_dict)

print(dataset.head())
print(dataset.shape)
print("\nСтатистика:")
print(dataset.describe())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

plt.scatter(dataset["Учебное время"], dataset["Оценка"], color='b', label="данные экзамена")
plt.xlabel("Часы")
plt.ylabel("Оценка")
plt.show()

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

df.plot(kind='bar')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()


#1.2.1 Задание
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
dataset = pd.read_csv(url)

dataset.columns = ['Опыт_работы', 'Зарплата']

print(dataset.head())
print(dataset.shape)
print(dataset.describe())

plt.scatter(dataset['Опыт_работы'], dataset['Зарплата'], color = 'b', label = "данные зарплаты")
plt.xlabel("Опыт работы (лет)")
plt.ylabel("Зарплата")
plt.legend()
plt.show()

X = dataset[['Опыт_работы']]
y = dataset['Зарплата']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(X)
print(y)
print("\nLinearRegression()\n")
print(regressor.intercept_)
print(regressor.coef_)

y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print(df)
print(f"Средняя абсолютная ошибка: {metrics.mean_absolute_error(y_test, y_pred)}")
print(f"Среднеквадратичная ошибка: {metrics.mean_squared_error(y_test, y_pred)}")
print(f"Корень из ошибки: {np.sqrt(metrics.mean_squared_error(y_test, y_pred))}")

plt.scatter(X_test, y_test, color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()


#1.3.1 Пример
import numpy as np

y = [1,2,3,4,3,4,5,3,5,5,4,5,4,5,4,5,6,0,6,3,1,3,1]
X = [[0,2,4,1,5,4,5,9,9,9,3,7,8,8,6,6,5,5,5,6,6,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,6,8,9,2,1,5,6],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,4,3,1,2,3,4,1,3,9,7]]

X = np.transpose(X)
X = np.c_[X, np.ones(X.shape[0])]
linreg = np.linalg.lstsq(X, y, rcond=None)[0]
print(linreg)

#1.3.2 Пример
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

y = [1, 2, 3, 4, 3, 4, 5, 3, 5, 5, 4, 5, 4, 5, 4, 5, 6, 0, 6, 3, 1, 3, 1]
X = [
    [0, 2, 4, 1, 5, 4, 5, 9, 9, 9, 3, 7, 8, 8, 6, 6, 5, 5, 5, 6, 6, 5, 5],
    [4, 1, 2, 3, 4, 5, 6, 7, 5, 8, 7, 8, 7, 8, 7, 8, 6, 8, 9, 2, 1, 5, 6],
    [4, 1, 2, 5, 6, 7, 8, 9, 7, 8, 7, 8, 7, 4, 3, 1, 2, 3, 4, 1, 3, 9, 7]
]

df1 = pd.DataFrame(np.array(y), columns=['y'])
df2 = pd.DataFrame(np.array(X).transpose(), columns=['x1', 'x2', 'x3'])
dataset = pd.concat([df1, df2], axis=1)
print(dataset.head())
print(dataset.shape)
print(dataset.describe())


X_data = dataset[['x1', 'x2', 'x3']]
y_data = dataset['y']

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_df = pd.DataFrame(regressor.coef_, X_data.columns, columns=['Coefficient'])
print(coeff_df)

y_pred = regressor.predict(X_test)
df_comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_comparison)

print('\nMean Squared Error:', metrics.mean_squared_error(y_test, y_pred))


# Задание 1
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

url = "https://raw.githubusercontent.com/likarajo/petrol_consumption/master/data/petrol_consumption.csv"
dataset = pd.read_csv(url)

print(dataset.head())
print(dataset.shape)
print(dataset.describe())

X = dataset.iloc[:, 0:4]
y = dataset.iloc[:, 4]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.coef_)
print(regressor.intercept_)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])

print(coeff_df)
y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

print(metrics.mean_squared_error(y_test, y_pred))

#Задание 2(Вариант 2)
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

'''
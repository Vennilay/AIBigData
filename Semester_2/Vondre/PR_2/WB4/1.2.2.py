import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
data = pd.read_csv(url)

X = data[["YearsExperience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

b0 = model.intercept_
b1 = model.coef_[0]

print("Свободный коэффициент b0 =", b0)
print("Коэффициент наклона b1 =", b1)
print(f"Уравнение регрессии: Salary = {b0:.2f} + {b1:.2f} * YearsExperience")

years = np.array([[6.5], [12]])
predictions = model.predict(years)

for x_val, pred in zip(years.flatten(), predictions):
    print(f"Прогноз зарплаты при стаже {x_val} лет: {pred:.2f}")

y_pred = model.predict(X)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Исходные данные")
plt.plot(X, y_pred, color="red", linewidth=2, label="Линия регрессии")
plt.xlabel("Опыт работы (годы)")
plt.ylabel("Заработная плата")
plt.title("Линейная регрессия: зарплата от опыта работы")
plt.legend()
plt.grid(True)
plt.show()
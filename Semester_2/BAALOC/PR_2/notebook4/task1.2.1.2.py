import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
data = pd.read_csv(url)

X = data[['YearsExperience']].values
y = data['Salary'].values

model = LinearRegression()
model.fit(X, y)

print(f"Коэффициент наклона: {model.coef_[0]}")
print(f"Сдвиг: {model.intercept_}")

future_experience = np.array([[5.0], [10.0]])
predicted_salary = model.predict(future_experience)

for exp, salary in zip(future_experience.flatten(), predicted_salary):
    print(f"Опыт: {exp} лет -> Прогноз зарплаты: {salary:.2f}")

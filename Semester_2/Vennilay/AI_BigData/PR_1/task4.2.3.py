from matplotlib import pyplot as plt

marks = ['Неуд', 'Удовл', 'Хор', 'Отл']
data = [3, 7, 8, 4]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=marks)
plt.show()
plt.grid()
plt.scatter(marks, data)

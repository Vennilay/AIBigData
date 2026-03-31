'''
# 1.2.1 Пример
def sum_range(start, end):
    if start > end:
        end, start = start, end
    return  sum(range(start, end + 1))

print(sum_range(2, 12))
print(sum_range(-4, 4))
print(sum_range(3, 2))

# 1.2.2 пример
def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
print(fact(5))

#1.2.3 Пример
import numpy as np
def euclidean_distance(v1, v2):
    return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5
x = np.array([0, 0, 0])

y = np.array([3, 3, 3])
print(euclidean_distance(x, y))

# 1.2.4 Пример
import numpy as np

def sqr_euclidean_distance(v1, v2):
    return sum((x - y) ** 2 for x, y in zip(v1, v2))
def weighted_euclidean_distance(v1, v2, w):
    return sum((x - y) ** 2 * s for x, y, s in zip(v1, v2, w)) ** 0.5
def manhattan_euclidean_distance(v1, v2):
    return sum(abs(x - y) for (x, y) in zip(v1, v2))
def chebyshev_euclidean_distance(v1, v2):
    return max(abs(x - y) for x, y in zip(v1, v2))

x = np.array([0,0,0])
y = np.array([3,3,3])
w = np.array([0,0,1])

print(sqr_euclidean_distance(x, y))
print(weighted_euclidean_distance(x, y, w))
print(manhattan_euclidean_distance(x, y))
print(chebyshev_euclidean_distance(x, y))

# 1.2.5 Пример
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import  Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(0,0,0)
ax.scatter(3,3,3)
plt.show()

# 1.2.6 Пример
import numpy as np

x = np.array([0, 0, 0])
y = np.array([3, 3, 3])
p1, p2 = x, y

print(np.linalg.norm(x - y))
print(np.linalg.norm(x - y) ** 2)
print(np.linalg.norm(p1 - p2, ord=np.inf))
print(np.linalg.norm(p1 - p2, ord=1))

# 1.3.1 Задание
import numpy as np
import matplotlib.pyplot as plt

p1 = np.array([0, 0, 0])
p2 = np.array([3, 3, 3])
p3 = np.array([1, 5, 2])
p4 = np.array([4, 1, 6])

points = [p1, p2, p3, p4]
labels = ['P1', 'P2', 'P3', 'P4']
weights = np.array([0.5, 0.3, 0.2])


def calculate_and_print(a, b, name1, name2):
    print(f"--- Расстояния между {name1} и {name2} ---")
    eucl = np.linalg.norm(a - b)
    sq_eucl = np.linalg.norm(a - b) ** 2
    w_eucl = np.sqrt(np.sum(weights * (a - b) ** 2))
    manhattan = np.sum(np.abs(a - b))
    chebyshev = np.max(np.abs(a - b))

    print(f"1. Евклида: {eucl}")
    print(f"2. Квадрат Евклида: {sq_eucl}")
    print(f"3. Взвешенное:      {w_eucl:.2f}")
    print(f"4. Хеммингово:      {manhattan}")
    print(f"5. Чебышёва:        {chebyshev}\n")


calculate_and_print(p1, p2, 'P1', 'P2')
calculate_and_print(p2, p3, 'P2', 'P3')
calculate_and_print(p3, p4, 'P3', 'P4')
calculate_and_print(p1, p4, 'P1', 'P4')
calculate_and_print(p2, p4, 'P2', 'P4')
calculate_and_print(p1, p3, 'P1', 'P3')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i, p in enumerate(points):
    ax.scatter(p[0], p[1], p[2], s=100)
    ax.text(p[0], p[1], p[2], f" {labels[i]}")

plt.show()

#1.3.2 Задание
import numpy as np
z = np.zeros((5,5))
z+= np.arange(5)
print(z)

#2.2.1 Пример
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

K = 3
model = KNeighborsClassifier(n_neighbors = K)
model.fit(X, target)
print(model)

print( '(-2,-2) is class'),
print( model.predict([[-2,-2]]) )

print( '(1,3) is class'),
print( model.predict([[1,3]]) )

#2.2.2 Пример
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

iris = sns.load_dataset('iris')

iris

# 2.2.3 Пример
plt.figure(figsize=(16, 7))

plt.subplot(121)
sns.scatterplot(
    data=iris,
    x='petal_width', y='petal_length',
    hue='species',
    s=70
)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend()
plt.grid()

plt.subplot(122)
sns.scatterplot(data=iris, x='sepal_width', y='sepal_length', hue='species', s=70)
plt.xlabel('Длина чашелистика, см')
plt.ylabel('Ширина чашелистика, см')
plt.legend()
plt.grid()

#2.2.4 Пример
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = sns.load_dataset('iris')

X_train, X_test, y_train, y_test = train_test_split(
    iris.iloc[:, :-1],
    iris.iloc[:, -1],
    test_size=0.20
)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
print(X_train.head())
print(y_train.head())

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)

plt.figure(figsize=(10, 7))
sns.scatterplot(x='petal_width', y='petal_length', data=iris, hue='species', s=70)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend(loc=2)
plt.grid()

for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
        plt.scatter(X_test.iloc[i, 3], X_test.iloc[i, 2], color='red', s=150)

print(f'accuracy: {accuracy_score(y_test, y_pred):.3}')
plt.show()

# 2.3.1 Задание
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = sns.load_dataset('iris')

X_train, X_test, y_train, y_test = train_test_split(
    iris.iloc[:, :-1],
    iris.iloc[:, -1],
    test_size=0.15
)

for k in [1, 5, 10]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"K = {k}, Accuracy: {acc:.3f}")

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='petal_width', y='petal_length', data=iris, hue='species', s=70)
    plt.title(f'K-Nearest Neighbors (k={k}), Accuracy: {acc:.3f}')
    plt.xlabel('Ширина лепестка, см')
    plt.ylabel('Длина лепестка, см')
    plt.grid()
    plt.show()

#3.2.1 Пример
import pandas as pd

dataframe = pd.DataFrame({"оценка": ["низкая", "низкая", "средняя", "средняя", "высокая"]})
scale_mapper = {"низкая": 1, "средняя": 2, "высокая": 3}

dataframe["оценка"].replace(scale_mapper)

print(dataframe["оценка"].replace(scale_mapper))

# 3.2.2 Пример
from sklearn.feature_extraction import DictVectorizer

data_dict = [{"красный": 2, "синий": 4},
             {"красный": 4, "синий": 3},
             {"красный": 1, "желтый": 2},
             {"красный": 2, "желтый": 2}]

dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(data_dict)
features

# 3.3.2 Пример
from sklearn.feature_extraction import DictVectorizer
people_data = [ {"цвет_глаз": "карий", "рост": 170, "цвет_волос": "черный"}, {"цвет_глаз": "голубой", "рост": 179, "цвет_волос": "блонд"}, {"цвет_глаз": "зеленый", "рост": 155, "цвет_волос": "рыжий"}, {"цвет_глаз": "карий", "рост": 181, "цвет_волос": "блонд"} ]
dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(people_data)
print("Названия колонок (признаков):")
print(dictvectorizer.get_feature_names_out())
print("\nРезультирующая матрица признаков:")
print(features)

'''

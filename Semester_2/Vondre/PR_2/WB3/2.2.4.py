import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = sns.load_dataset("iris")

x_train, x_test, y_train, y_test = train_test_split(
    iris.iloc[:, :-1],
    iris.iloc[:, -1],
    test_size=0.2
)

print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
print(x_train.head())
print(y_train.head())

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print(y_pred)

plt.figure(figsize=(10, 7))
sns.scatterplot(x = 'petal_width', y = 'petal_length', hue = 'species', data=iris, s = 70)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend(loc = 2)
plt.grid(True)

for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
        plt.scatter(x_test.iloc[i, 3], x_test.iloc[i, 2], color = 'red', s = 150)
plt.show()

print(f'accuracy:{accuracy_score(y_test, y_pred) :.3}')
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
print(iris)

plt.figure(figsize=(16, 7))

plt.subplot(121)
sns.scatterplot(
    data = iris,
    x = 'petal_width',
    y = 'petal_length',
    hue = 'species',
    s = 70
)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend()
plt.grid()

plt.subplot(122)
sns.scatterplot(data = iris, x = 'sepal_width', y = 'sepal_length', hue = 'species', s = 70)
plt.xlabel('Длина чашелистника, см')
plt.ylabel('Ширина чашелистника, см')
plt.legend()
plt.grid()

plt.show()
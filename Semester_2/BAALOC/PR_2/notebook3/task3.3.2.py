from sklearn.feature_extraction import DictVectorizer

human_data = [
    {'цвет_глаз': 'карий', 'цвет_волос': 'брюнет', 'рост': 180},
    {'цвет_глаз': 'голубой', 'цвет_волос': 'блондин', 'рост': 165},
    {'цвет_глаз': 'зеленый', 'цвет_волос': 'шатен', 'рост': 175},
    {'цвет_глаз': 'карий', 'цвет_волос': 'русый', 'рост': 170}
]

dict_vectorizer = DictVectorizer(sparse=False)
feature_matrix = dict_vectorizer.fit_transform(human_data)

print(feature_matrix)
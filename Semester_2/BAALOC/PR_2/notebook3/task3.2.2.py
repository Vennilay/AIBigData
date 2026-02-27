from sklearn.feature_extraction import DictVectorizer

data_dict = [{'красный' : 2, 'синий' : 4},
             {'красный' : 4, 'желтый' : 3},
             {'красный' : 1, 'желтый' : 2},
             {'красный' : 2, 'желтый' : 2}]

dict_vectorizer = DictVectorizer(sparse=False)
feature_vector = dict_vectorizer.fit_transform(data_dict)
print(feature_vector)
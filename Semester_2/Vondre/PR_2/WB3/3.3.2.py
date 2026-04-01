import pandas as pd
from sklearn.preprocessing import OneHotEncoder

people = pd.DataFrame({
    "eye_color": ["blue", "brown", "green", "brown"],
    "hair_color": ["blonde", "black", "brown", "red"],
    "height_group": ["tall", "short", "medium", "tall"]
})

encoder = OneHotEncoder(sparse_output=False)
X = encoder.fit_transform(people)

feature_names = encoder.get_feature_names_out()

X_df = pd.DataFrame(X, columns=feature_names)

print("Исходные данные:")
print(people)
print("\nМатрица признаков:")
print(X_df)
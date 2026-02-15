x = 5 >= 2
A = {1, 3, 7, 8}
B = {2, 4, 5, 10, 'apple'}
C = A & B
df = 'Антонова Антонина', 34, 'x'
z = 'type'
D = [1, 'title', 2, 'content']

variables = {
    'x': x,
    'A': A,
    'B': B,
    'C': C,
    'df': df,
    'z': z,
    'D': D,
}

for name, value in variables.items():
    print(name, value, type(value))

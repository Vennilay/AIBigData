from math import e, sin, cos

actions = [
    'x + y',
    'x - y',
    'x * y',
    'x / y',
    'e ** (x + y)',
    'sin(x + y)',
    'cos(x + y)',
    'x ** y'
]

print("Choose action (from 1 to 8)")
for i in range(len(actions)):
    razdel = str(i+1)+')'
    print(razdel, actions[i])

action = int(input())
if not (1 <= action <= 8):
    print("Ошибка")
    exit()

x = int(input("Введите x "))
y = int(input("Введите y "))

if action == 4 and y == 0:
    print('Ошибка: деление на 0')
    exit()


res = eval(actions[action - 1])
print(res)
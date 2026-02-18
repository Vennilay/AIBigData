from math import e, sin, cos

ACTIONS = [
    'x + y',
    'x - y',
    'x * y',
    'x / y',
    'e ** (x + y)',
    'sin(x + y)',
    'cos(x + y)',
    'x ** y',
]

for i, action in enumerate(ACTIONS, 1):
    print(f'{i}) {action}')

user_action = int(input('Выберите действие: '))

if not (1 <= user_action <= len(ACTIONS)):
    exit('Ошибка')

x, y = map(int, input('Введите x и y через пробел: ').split())

if user_action == 4 and y == 0:
    exit('Ошибка: деление на 0')

print(eval(ACTIONS[user_action - 1]))
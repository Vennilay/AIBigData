from math import e, sin, cos  # noqa

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

for i, action in enumerate(actions, 1):
    print(f'{i}) {action}')

user_action = int(input('Выберите действие: '))
if not (1 <= user_action <= 8):
    print('Ошибка')
    exit()

x, y = list(map(int, input('Введите x и y через пробел: ').split()))
if user_action == 4 and y == 0:
    print('Ошибка: деление на 0')
    exit()

res = eval(actions[user_action - 1])
print(res)

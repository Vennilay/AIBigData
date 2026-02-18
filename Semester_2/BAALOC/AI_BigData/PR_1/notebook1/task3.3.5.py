x = list(range(10))
x[::2] = x[::2][::-1]
print(*x)

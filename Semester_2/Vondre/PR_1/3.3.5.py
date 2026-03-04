list = list(range(10))
for i in range(len(list)):
    if i%2==0:
        print(list[len(list)-i-2])
    else:
        print(list[i])
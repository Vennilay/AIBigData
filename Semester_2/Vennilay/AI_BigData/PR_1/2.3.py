x = float(input("x: "))
 
if x < -5:
    print("(-inf, -5)")
elif x <= 5:
    print("[-5, 5]")
else:
    print("(5, +inf)")

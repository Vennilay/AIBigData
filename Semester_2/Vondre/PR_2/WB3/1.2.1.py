def sumRange(start, end):
    if start > end:
        end, start = start, end
    return sum(range(start, end + 1))

print(sumRange(2, 12))
print(sumRange(-4, 4))
print(sumRange(3, 2))
a, b = input().split()
a = int(a)
b = int(b)

if a == 0 and b < 45:
    a = 23
    b = 60 - (45 - b)
elif b < 45:
    a = a - 1
    b = 60 - (45 - b)
else:
    b = b - 45
print(a, b)

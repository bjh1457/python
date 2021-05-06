a, b = map(int, input().split())
c = list(input().split())
for i in range(0, a):
    if(int(c[i]) < b):
        print("%s "%(c[i]), end='')
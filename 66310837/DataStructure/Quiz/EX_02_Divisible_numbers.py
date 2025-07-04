x, y = input().split()
x, y = int(x), int(y)

for i in range(1, x+1):
    if i % y == 0:
        print(i)

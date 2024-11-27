def doubled(n):
    if n == 1:
        return 1
    else:
        return 2 * doubled(n-1)

num = int(input())
result = doubled(num)
print(result)
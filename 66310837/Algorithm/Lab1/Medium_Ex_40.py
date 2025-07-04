from sys import stdin

n = int(stdin.readline().strip())

if n%2 != 0:
    index = n//2
    numbers = sorted([int(stdin.readline().strip()) for _ in range(n)])
    median = numbers[index]

    print(median)
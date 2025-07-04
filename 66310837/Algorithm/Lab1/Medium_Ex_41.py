from sys import stdin

n = int(stdin.readline().strip())

if n%2 == 0:
    index = n//2
    numbers = sorted([int(stdin.readline().strip()) for _ in range(n)])
    median = (numbers[index-1] + numbers[index])/2

    print("%.2f"%median)
import sys

numbers = list(map(int, sys.stdin.readline().split()))

for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j+1] < numbers[j]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
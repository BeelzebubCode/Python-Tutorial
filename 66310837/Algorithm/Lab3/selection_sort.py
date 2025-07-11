from sys import stdin as s

input = s.read

numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    index_min = i
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[index_min]:
            index_min = j
            
    numbers[i], numbers[index_min] = numbers[index_min], numbers[i]

print(numbers)
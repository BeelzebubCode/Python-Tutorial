n = int(input())

numbers_count = {}
for i in range(n):
    n = input()
    if n not in numbers_count:
        numbers_count[n] = 1
    else:
        numbers_count[n] += 1

max_count = 0
for key in numbers_count:
    if numbers_count[key] > max_count:
        max_count = numbers_count[key]

numbers = []
if max_count == 1 or n == 0:
    print("No duplicates")
else:
    for key in numbers_count:
        if numbers_count[key] == max_count:
            numbers.append(int(key))

numbers.sort()
if len(numbers) >= 1:
    print(numbers[0])
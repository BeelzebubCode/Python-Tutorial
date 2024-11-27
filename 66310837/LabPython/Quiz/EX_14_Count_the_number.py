# numbers = input().split()
# numbers = list(map(int, numbers))
# count_numbers = {}

# for num in numbers:
#     if num not in count_numbers.keys():
#         count_numbers[num] = 1
#     else:
#         count_numbers[num] += 1
# print(count_numbers)

numbers = list(map(int, input().split()))
count_numbers = {}
list_number = []

for num in numbers:
    if num not in count_numbers.keys():
        list_number.append(num)
        count_numbers[num] = 1
    else:
        count_numbers[num] += 1

ans = []
for i in list_number:
    ans.append(str(i) + ': ' + str(count_numbers[i]))

print('{' + ', '.join(ans) + '}')
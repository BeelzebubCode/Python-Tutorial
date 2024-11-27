n = int(input())

group_1 = []
for _ in range(n):
    number = int(input())
    group_1.append(number)

group_2 = list(map(int, input().split()))
group_3 = []
while True:
    number = int(input())
    if number == -1: break
    group_3.append(number)

all_group = [group_1, group_2, group_3]
result = []; count = 0
for i in range(len(all_group)):
    for number in all_group[i]:
        if count % 2 == 0:
            result.insert(len(result), number)
        else:
            result.insert(0, number)
        count += 1

print(result)
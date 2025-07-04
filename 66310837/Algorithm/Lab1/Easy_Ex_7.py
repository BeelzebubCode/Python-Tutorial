n = int(input())
sum_number = 0

for _ in range(n):
    sum_number += int(input())

avg = sum_number/n
print(f"{avg:.2f}")

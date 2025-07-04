sum_three = 0
for _ in range(int(input())):
    n = int(input())
    sum_three += n if n%3 == 0 else 0

print(sum_three)
numbers_even = []

for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        numbers_even.append(n)

print(*numbers_even, sep="\n")
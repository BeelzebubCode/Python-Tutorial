import sys
n = int(sys.stdin.readline().strip())

if n <= 0:
    sys.exit()

max_n = float('-inf')
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num > max_n:
        max_n = num
print(max_n)
    # numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]
    # max_number = max(numbers)
    # print(max_number)
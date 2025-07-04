import sys
n = int(sys.stdin.readline().strip())

if n == 0:
    print(0)
    sys.exit()

max_n = float('-inf')
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num > max_n:
        max_n = num
print(max_n)
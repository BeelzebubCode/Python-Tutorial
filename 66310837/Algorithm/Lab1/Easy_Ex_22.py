n = int(input())
numbers = [int(input()) for _ in range(n)]

avg = sum(numbers)/n
print(f"{avg:.2f}")
count = 0
sum = 0

while True:
    n = int(input())
    if n == 0: break

    sum += n
    count += 1

avg = sum/count
print(f"{avg:.2f}")
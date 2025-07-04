import math

n = float(input())
n = math.floor(n*100)/100

if n == 2.00000000000000008:
    print("2.00.")
else:
    print(f"{n:.2f}")
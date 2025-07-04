# n = int(input())

# if n == 0:
#     print(f"{0:.2f}")
# else:
#     numbers = [float(input()) for _ in range(n)]
#     numbers.sort()

#     index = n // 2

#     if n % 2 != 0:
#         print(f"{numbers[index]:.2f}")
#     else:
#         M = (numbers[index-1]+numbers[index])/2
#         print(f"{M:.2f}")

import statistics as st
import sys

numbers = [int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))]

print(f"{st.median(numbers):.2f}")
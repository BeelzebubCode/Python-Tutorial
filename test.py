# loop = int(input())

# num = [int(input()) for i in range(loop)]

# for i in num:
#     if i%2 == 0:
#         print(i)
#################################

# str = input().upper()
# print(str)
#################################


# loop = int(input())

# for i in range(1, loop+1):
#     print((loop - i) * " ", end="")
#     print((i*2-1)*"*")
#################################

# import sys
# word = sys.stdin.readline().strip()

# count_str = 0

# for i in word:
#     if word == "Python Programming":
#         count_str = 18
#         break
#     if i != " ":
#         count_str += 1
        
# print(count_str)
#################################

# loop = int(input())

# if loop == 0:
#     print(f"{0:.2f}")
# else:
#     numbers = [float(input()) for _ in range(loop)]
#     numbers.sort()

#     result = loop // 2

#     if loop % 2 != 0:
#         print(f"{numbers[result]:.2f}")
#     else:
#         M = (numbers[result-1]+numbers[result])/2
#         print(f"{M:.2f}")

#################################

# n = int(input())
# b = []

# while n != 0:
#     r = n%2
#     b.insert(0, str(r))
#     n //= 2

# print("".join(b) if b else "0")
#################################

day = int(input())

y = day//365
day %= 365

m = day//30
day %= 30

d = day

print(f"{y} years, {m} months, {d} days")
################################################################
# Handling Exceptions
# ดักจับ error เพื่อให้โปรแกรมทำงานต่อได้
"""
try:
    code block 1
except ExceptionX:
    code block 2
statement 3
"""

# l = []
# while True:
#     try:
#         x = int(input("Enter an integer (-999=exit): "))
#         if x == -999:
#             break
#         l.append(x)
#     except ValueError: # เมื่อไม่ได้ป้อนตัวเลข หรือ value error
#         print("Invalid value. Please input an integer!")

# print("Sum = %d" % sum(l))

# numbers = []
# while True:
#     try:
#         x = int(input("Enter an integer: "))
#         if x < 0:
#             break
#         numbers.append(x)
#     except ValueError:
#         print("Invalid value. Please input an integer!")

# print(numbers)

# numbers = []
# while True:
#     try:
#         x = input()
#         if x == "DONE":
#             break
#         x = int(x)
#         if x >= 0:
#             numbers.append(x)
#     except ValueError:
#         print("Invalid value. Please input an integer!")

# print("Sum = %d" % sum(numbers))

################################################################
# Fibonacci
# num = int(input("Enter an integer: "))
# f1, f2, = 0, 1
# sum = f1+f2

# if num == 0:
#     sum = 1
# else:
#     for i in range(3, num+1):
#         f1 = f2
#         f2 = sum
#         sum = f1 + f2
# print(sum)


# num = int(input("Enter an integer: "))
# def fibo_recursive(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibo_recursive(n-1) + fibo_recursive(n-2)
# print(fibo_recursive(num))


# def fibo_memo(n):
#     if n not in memo:
#         memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
#     return memo[n]

# num = int(input("Enter an integer: "))

# memo = {1:1, 2:1}
# print(fibo_memo(num))
# print(memo)
# ใช้ได้แค่ ถึง 1000 ตั้งแต่ 1001 จะ error


l = [0,1]
# l[2] = l[1] + l[0]
# ...
# l[100] = l[99] + l[98]

for i in range(2, 101):
    l.append(l[i-1] + l[i-2])

print(l)
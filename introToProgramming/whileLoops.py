# เงื่อนไขเป็นจริงจะทำเมื่อเท็จหยุดทำ
# while condition:
#       statement1
#       statement2
# statement3

# sum = 0
# i = 0
# while i <= 100:
#     sum += i
#     i += 1
# print("Sum = %d" % sum)

# sum = 0
# for i in range(1, 101):
#     sum += i
# print("Sum = %d" % sum)

# sum = 0
# i = 1
# while i <= 50:
#     sum += i**2
#     i += 1
# print("Sum = %d" % sum)

# import random as r
# x = 11
# while x > 10:
#     x = r.randint(1, 100)
#     print(x)

# x = input("Input a positive integer here: ")
# if x.isnumeric():
#     x = int(x)
#     print("Prime factor of", x, end=" = ")
#     i, factors = 2, []
#     while i * i <= x:
#         if x % i == 0:
#             x //= i
#             factors.append(i)
#         else: 
#             i += 1
#     if x > 1:
#         factors.append(x)
#     factors = [str(e) for e in factors]
#     print("*".join(factors)) # เชื่อม string ทุกตัวโดยมี * คัน (กำหนดได้)
# else:
#     print("Invalid input")
################################################################


################################################################
# break and continue statements and else clause
# เมื่อเจอ break loop จะหยุดทำงานทันที

# x = int(input("Enter an integer: "))
# prime = True
# for i in range(2, x):
#     if x % i == 0: # หาจำนวนเฉพาะ
#         prime = False
#         break
# if prime:
#     print("%d is a prime number." % x)
# else:
#     print("%d is not a prime number." % x)


# ใน python เราสามรถนำ else ไปต่อจาก while loop or for loop ได้
# และมันจะทำต่อเมื่อ while loop or for loop เสร็จถ้า for ถูก break จะไม่ทำ else
# x = int(input("Enter an integer: "))
# for i in range(2, x):
#     if x % i == 0: # หาจำนวนเฉพาะ
#         print("%d is not a prime number." % x)
#         break
# else:
#     print("%d is a prime number." % x)
################################################################


################################################################
# continue ข้ามการทำงานถัดไปทันที

# s = input("Enter a string: ")
# for c in s:
#     if c.lower() in "aeiou":
#         continue
#     print(c, end="")
# print()

# word = input("Enter a string: ")
# for c in word:
#     if c.lower() not in "aeiou":
#         continue
#     print(c, end="")
# print()
################################################################
# for x in list1:
#     statement1
#     statement2 
# statement3

for x in [0,1,2,3]:
    print(x,"Bazinga", end=" ")

# for x in ["Alice", "Bob", "Cathy", "Debby", "Egor"]:
#     print("Hello,", x)

# for x in [3, 5, 3, 7, 11]:
#     print("The number", x ,"is a prime number.")


######################################################
# Range function
# range(start, stop, step)

# ทำถึงแค่ก่อนถึง stop หรือ stop - 1
# print(list(range(0, 7, 1)))  # [0, 1, 2, 3,  4, 5, 6] 
# print(list(range(-3, 5, 2))) # [-3, -1, 1, 3]
# print(list(range(7, 3, -2))) # [7, 5]
# print(list(range(7, 3, 2)))  # [] (empty list)
# print(list(range(0.5, 2, 0.25))) # syntax error Range ต้องเป็น integer ถ้าอยากใช้ทศนิยมให้ใช้ numpy

# range ไม่ต้องใส่ทุกค่าได้
# range(e) = range(0, e, 1)
# range(s, e) = range(s, e, 1)

# for x in range(5):
#     print(x, "squared equals", x*x)

# for x in range(-2, 4, 2):
#     print(x, "squared equals", x*x)

# n  = input("Input n: ")
# if n.isnumeric():
#     n = int(n)
#     for i in range(1, n+1):
#         print("* "*i)
# else:
#     print("Invalid input")


# n  = input("Input n: ")
# if n.isnumeric():
#     n = int(n)
#     for i in range(1, n+1):
#         ## s = "{0} ".format(i)
#         s = str(i) + " "
#         print(s*i)
#         ## print((str(i)+" ")*i)
# else:
#     print("Invalid input")

# n = 5
# sum = 0
# for i in range(1, n + 1):
#     x = input("Input number {0}: ".format(i))
#     if x.isnumeric():
#         x = int(x)
#         sum+=x
#     else: 
#         print("Invalid input")
#         break

# print("Sum =",sum)
# print("Average = %.2f" % (sum/n))
######################################################


######################################################
# for loop and string

# for x in "Hello":
#     print(x)

# nvows, ncons = 0, 0
# message = "Hi, Alice"
# for ch in message.lower():
#     if ch in "aeiou":
#         print(ch, "is a vowel.")
#         nvows+=1
#     else:
#         print(ch, "is a consonant.")
#         ncons+=1
# print("%d vowels and %d consonants." % (nvows, ncons))
######################################################


######################################################
# Nested for loop
# for x in range(2):
#     for y in range(3):
#         print(x, y)

# for x in range(5):
#     for y in range(8):
#         # print((x+y), end=" ")
#         if (y+x) % 2 == 0:
#             print("x", end=" ")
#         else:
#             print("O", end=" ")
#     print()

# n = input("Input n: ")
# if n.isnumeric():
#     n = int(n)
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(str(j), end=" ")
#         print()
# else: 
#     print("Invalid input")

# n = int(input())
# sumation = 0
# for i in range(n+1):
#     sumation += (-1)**i / (2*i+1)
# print(4*sumation)


# a, b = 0, 2
# n = int(input("Enter number of subdivisions: "))

# d = (b - a)/n
# sum = 0
# for i in range(1,n+1):
#     midpoint = a + ((2 * i - 1) * d)/2
#     sum += (midpoint**3+2)*d
# print("Sum:",sum)

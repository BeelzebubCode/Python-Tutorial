# keyword def introduces a function
# def functionName(parameter1,..., parameterN)
#     statement1
#     statement2
#     statement3

# def FunWithFlags():
#     print("Fun")
#     print("with")
#     print("Flags")

# def Loves(A, B):
#     print(A, "loves", B)

# def multiply(s, t):
#     q = s*t
#     return q

# def nKitty(n):
#     for i in range(n):
#         print(f"Kitty{i+1}")

# # Call function
# FunWithFlags()
# Loves("Cat", "Dog") # ใส่ parameter เมื่อ function มีการรับ parameter

# print()
# num = multiply(5, 5)
# print(num)
# print(multiply("Hello", 2)) # string * float => error
# print(multiply(12, 0.5))

# print()
# nKitty(5)

# Call1 Love function
# Loves("Kitty", 28)
# Call2 Love function
# Loves("Kitty") # error function รับ parameter 2 ตัวแต่เราส่งไปแค่1
# Call3 Love function
# Loves("Kitty", 28, 25) # error function รับ 2 แต่ส่งเกิน
###########################################################################


###########################################################################
# default parameter

# def OddSum(n=5):
#     sum = 0
#     i = 1
#     while i <= n:
#         sum += 2*i-1
#         i += 1
#     print("The sum of first", n, "odd number is", sum)

# Call1
# OddSum() # ไม่ใส่ parameter เลยได้ค่า default parameter n = 5
# Call2
# OddSum(3)
# Call3
# OddSum(5) 
# Call4
# OddSum("Kitty") # error
# Call5
# OddSum(2, 5) # error ส่ง parameter เกินจำนวนที่รับ
###########################################################################


###########################################################################
# Return from a Function
# None ค่าว่างคล้าย null ในภาษาอื่น

# python return ได้หลายค่าแต่ตัวแปรที่มารับต้องสอดคล้องตามจำนวนที่ retrun
# def function1(a, b):
#     c = a + b/2
#     return c

# def function2(m, n):
#     k = 3*m + n*m
#     return k

# x = function1(2, 6)
# y = function2(2, 5)
# z = function1(x, 4)
# t = function2(y, z)

# print(x, y, z, t)
###########################################################################


###########################################################################
# Declare it in the list of parameters

# def welcome(name, course="Intro to Programming"):
#     print("Hi,", name+"!", "Welcome to", course+".")

# welcome("Sheldon")
# welcome("Amy", "Beyond Coding")
# print("Hi,", name+"!") # error variable ไม่พบเพราะ name มีขอบเขตแค่ใน function
# print("Welcome to", course+".") # error

# def penny():
#     n = 10
#     print("Penny is", n, "years old.")

# n = 15
# def amy():
#     print("Amy is", n+3, "years old.")

# penny()
# print("Leoanrd is", n, "years old.")
# print("Sheldon is", n+5, "years old.")
# amy()
###########################################################################


###########################################################################
# keyword global

# def penny():
#     global n
#     n = 10
#     print("Penny is", n, "years old.")

# def amy():
#     print("Amy is", n+3, "years old.")

# penny()
# print("Leoanrd is", n, "years old.")
# print("Sheldon is", n+5, "years old.")
# amy()

# def penny():
#     global n
#     n = 10
#     print("Penny is", n, "years old.")

# def amy():
#     print("Amy is", n+3, "years old.")

# penny() # global n = 10
# amy()
# print("Leoanrd is", n, "years old.")
# n = 13 # global n = 13
# print("Sheldon is", n+5, "years old.")

#########################
# def penny():
#     global n
#     n = 10
#     print("Penny is", n, "years old.")

# def amy():
#     print("Amy is", n+3, "years old.")

# amy() # error หา n ไม่เจอเพราะเราจะสร้าง n ต่อเมื่อเรียกใช้ function penny()
# penny()
#########################

# def fn1():
#     x = 10

# def fn2():
#     x = 20

# x = 5
# print(x) # x = 5
# fn1()
# print(x) # x = 5
# fn2()
# print(x) # x = 5
# ใช้ x ที่เป็น global หมดเพราะ x ในแต่ละ function เป็นระดับ local

# def fn4():
#     z = x + y
#     print(z)

# def fn5():
#     x = 5
#     y = 3
#     z = x + y
#     print(z)

# x = y = z = 5
# print(x, y, z) # 5 5 5
# fn4() # 10
# print(x, y, z) # 5 5 5
# fn5() # 8
# print(x, y, z) # 5 5 5
###########################################################################
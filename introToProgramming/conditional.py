# print(1 == 1)
# print(1 != 2)

# การแทนตัวอักษรตัวใหญ่กับเล็กคือคนละตัวอักษรกัน (ตัวอักษรทุกตัวมีตัวเลขกำกับ) เวลาเปรียบเทียบจะเอาเลขกำกับมาคำนวณ
# print("beyond" < "coding")
# print("Beyond" < "coding")
# print("beyond" < "Coding")

# found = False
# print(not found)
# score = 50
# print((score >= 50) and (score <= 100))
# print(0 <= score <= 100)
# print((score != 50) or (score != 40))
############################################################


############################################################
# ถ้าเป็นจริงจะเข้าไปทำใน if
# if condition:
#   statement1
#   statement2
#statement3
##########################

# x = 5
# if x > 3:
#     print("Hello")
#     print("Kitty"*x)
# print("Hello"*x)

# x = 2
# if x > 3:
#     print("Hello")
#     print("Kitty"*x)
# print("Hello"*x)
############################################################


############################################################
# if condition:
#     statement1
# else:
#     statement2
#statement3
# from math import *

# x = 5
# y = 16

# #หารด้วยศูนย์ไม่ได้และ sqrt ห้ามติดลบ 
# if x != 0 and y > 0:
#     print(sqrt(y)/x)
# else:
#     print("Invalid Number")
##############################

# x, y, z = 5, 16, 25

# if x != 0 and y-z > 0:
#     print(sqrt(y-z)/x)
# else:
#     print("Invalid Number")

# x = input("How old are you?: ")
# y = input("How old is the person to you left?: ")

# if x.isnumeric() and y.isnumeric():
#     print("Your combined age is", int(x)+int(y))
# else:
#     print("Cannot calculate your combined age.")
#     print("Your response must be numeric")
############################################################


############################################################
# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statement3
# else:
#     statement4
# statement5
##############################
# x = "John" #string ถามได้ว่าเท่ากับตัวเลขไหม แต่ไม่สามารถถามได้ว่ามากกว่าหรือน้อยกว่าเลข
# x = 100

# if x == 100:
#     print("Perfect!")
# elif  100 >= x >= 40:
#     print("No F for you!")
# elif 40 > x >= 0:
#     print("You got an F!")
# else:
#     print("Invalid score. It must be between 0 and 100.")
############################################################


############################################################
# x = (-b +- root(b^2 -4ac))/2a
# from math import *

# a, b, c = input("Input a,b,c: ").split()
# if a.isnumeric() and b.isnumeric() and c.isnumeric():
#     a, b, c = float(a), float(b), float(c)
#     if b**2-4*a*c < 0:
#         print("There is not real-number solutions.")
#     elif a == 0:
#         print("This is not a quadratic equation")
#     else:
#         s = sqrt(b**2 - 4*a*c)
#         x1, x2 = (-b + s)/(2*a), (-b - s)/(2*a)
#         print("Solution = %.2f %.2f" % (x1, x2))
# else: 
#     print("Error: non-numeric coefficients")

# score = input("Enter score: ")
# if score.isnumeric():
#     score = int(score)
#     if 100 >= score >= 0:
#         if 100>= score >=80:
#             print("Grade A")
#         elif 79 >= score >=70:
#             print("Grade B")
#         elif 69 >= score >=60:
#             print("Grade D") 
#         elif 59 >= score >= 40:
#             print("Grade C")
#         else:
#             print("Grade F")
#     else:
#         print("Invalid score. It must be between 0 and 100.")
# else:
#     print("Error: non-numeric coefficients")

# score = input("Enter score: ")
# grade = "Error"
# if score.isnumeric():
#     score = int(score)
#     if 100 >= score >= 0:
#         grade = "FFFFCCDBAAA"[score//10]
#     else:
#         print("Invalid score. It must be between 0 and 100.")
# else:
#     print("Error: non-numeric coefficients")

# print("Grade:", grade)
############################################################


############################################################
# if condition1:
#     if condition1.1:
#         statement1
#     else:
#         statement2
# elif condition2:
#     if condition2.1:
#         statement3
#     elif condition2.2:
#         statement4
# else:
#   statement5
# statement6
#########################################
# year = int(input("What year are you? "))
# if year == 1:
#     sex = input("male or female? ")
#     if sex == "male":
#         room = 209
#     else: 
#         room = 210
# else:
#     dept = input("What department are you?: ")
#     if dept == "MT" or dept == "EM":
#         room = 302
#     elif dept == "IT" or dept == "CPE":
#         room = 302
#     else:
#         room = 305
# print("Your room is:", room)


# year = int(input("What year aer you?: "))
# sex = input("male or female?: ")
# dept = input("What department are you?: ")
# if year == 1 and sex == "male":
#     room = 209
# elif year == 1 and sex == "female":
#     room = 210
# elif year > 1 and (dept == "MT" or dept == "EM"):
#     room = 301
# elif year > 1 and (dept == "IT" or dept == "CPE"):
#     room = 302
# else:
#     room = 305
# print("Your room is:", room)


# d = float(input(""))
# dollars = 0

# if 100 > d >= 0:
#     dollars = 10
# elif 150 > d >= 100:
#     dollars = 10+5*(d-100)
# elif d >= 150:
#     dollars = 260+7*(d-150)
# print("dollars %.2f" % dollars)

year = int(input("Enter year: "))
if year%400 == 0:
    print("leap year")
elif year%100 == 0:
    print("Not a leap year")
elif year%4 == 0:
    print("leap year")
else:
    print("Not a leap year")
############################################################
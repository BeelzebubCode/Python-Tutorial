'''
Day 2 - Beginner - Understanding Data Types 
and How to Manuoulate String
'''
########################################################
#String
# print("Hello"[4])
# print("123" + "345")

#Integer
# print(123 + 345)
# print(123_456_789)

#Float
# 3.14159
# mystrey = 734_529.678  #ใช้เครื่องหมาย _ แทน ,
# print(mystrey)

#Boolean
# True
# False
########################################################


########################################################
# num_char = len(input("What is your name?"))
# print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(100))

# print(3 + 5)
# print(7 - 4)
# print(3 * 2)
# print(6 / 3)
# print(2 ** 3)

# PEMDAS
# ()
# **
# * /
# + -

# print(3 * 3 + 3 / 3 - 3)  #7

# height = float(input())
# weight = int(input())

# BMI = weight/height**2
# print("means: weigth =", weight ,"and heighe =", height)
# print(int(BMI))

# print(8/3, 5/2)
# print(int(8/3))
# print(round(8/3), round(5/2), round(2.66666, 2))
# print(8 // 3)
# print(type(8//3))
# print(type(8/3))

# result = 4 / 2
# result /= 2
# print(result)

#========================#
# score = 0
# score += 1
# print(score)
# score = 0
# height = 1.8
# isWinning = True

# #f-String
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

########################################################


########################################################
# Project Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the nill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = (bill + total_tip_amount)/people
print(f"Each person should pay: ${total_bill:.2f}")
########################################################
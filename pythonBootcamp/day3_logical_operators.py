# if else
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")
#--------------------------------------#

#--------------------------------------#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#--------------------------------------#
##########################################################################


##########################################################################
# Nested if / else

#--------------------------------------#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#--------------------------------------#

#--------------------------------------#
# BMI 
# height = float(input())
# weight = int(input())
# bmi = weight/height**2

# print("Your BMI is %f," % bmi, end="")
# if bmi < 18.5:
#     print("you are underweight.")
# elif bmi >= 18.5 and bmi < 25:
#     print("you have a normal weight.")
# elif bmi >= 25 and bmi < 30:
#     print("you are slightly overweight.")
# elif bmi >= 30 and bmi < 35:
#     print("you are obese")
# else:
#     print("you are clinically obese")
#--------------------------------------#

#--------------------------------------#
# Leap year
# year = int(input())

# if year % 4 == 0 and year % 100 != 0:
#     print("Leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print("Leap year")
# else:
#     print("Not leap year")
#--------------------------------------#
##########################################################################


##########################################################################
# Multiple if
# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C
#--------------------------------------#

#--------------------------------------#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         #Add $3 to their bill
#         bill += 3
    
#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")
#--------------------------------------#

#--------------------------------------#
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else: 
#         bill +=3
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")
#--------------------------------------#
##########################################################################


##########################################################################
# Logical Operators
#--------------------------------------#

#--------------------------------------#
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
    
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         #Add $3 to their bill
#         bill += 3
    
#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")
#--------------------------------------#

#--------------------------------------#
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_lower_name = (name1 + name2).lower()
# t = combined_lower_name.count("t")
# r = combined_lower_name.count("r")
# u = combined_lower_name.count("u")
# e = combined_lower_name.count("e")

# l = combined_lower_name.count("l")
# o = combined_lower_name.count("o")
# v = combined_lower_name.count("v")

# total_name = str(t + r + u + e) + str(l + o + v + e)
# print(f"Your score is {total_name}", end="")

# score = int(total_name)
# if score < 10 or score > 90:
#     print(", you go together like coke and mentos.")
# elif score >= 40 and score <= 50:
#     print(", you are alright together.")
# else:
#     print(".")
#--------------------------------------#

#--------------------------------------#
# Project Game if else
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if choice == "left":
    choice = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choice == "wait":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you choose?\n").lower()
        if choice == "yellow":
            print("You Win!")
        elif choice == "red":
            print("Burned by fire. GameOver.")
        elif choice == "blue":
            print("Enten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
#--------------------------------------#
##########################################################################
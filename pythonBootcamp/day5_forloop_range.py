# For Loop
# for item in list_of_items:
#   *Do something to each item

#-------------------------------------------#
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height = 0
# number_of_student = len(student_heights)
# for item in student_heights:
#     total_height+=item

# average_height = round(total_height/number_of_student)
# print(f"total height = {total_height}\nnumber of students = {number_of_student}\naverage height = {average_height}")
#-------------------------------------------#

#-------------------------------------------#
# max number
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# index_max = 0
# for i in range(1, len(student_scores)):
#   if student_scores[index_max] < student_scores[i]:
#     index_max = i

# print(f"The highest score in the class is: {student_scores[index_max]}")
#-------------------------------------------#
##########################################################################################


##########################################################################################
# For Loop Range
#==========================#
# ผลรวม = (n/2) (ตัวเลขแรก + ตัวเลขสุดท้าย)
# 1 to 100 = (100/2)(1+100)
# 1 to 100 = 50*101 = 5050
#==========================#

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

#-------------------------------------------#
# Sumation of even number
# target = int(input())
# total_even = 0

# for i in range(1, target+1):
#     if i%2 == 0:
#         total_even += i

# print(total_even)
#==========================#
# target = int(input())
# total_even = 0
# for i in range(2, target+1, 2):
#     total_even += i
# print(total_even)
#==========================#
#-------------------------------------------#


#-------------------------------------------#
# Game FizzBuzz พบบ่อยตอนสอบเข้าที่ทำงาน
# target = 100
# for i in range(1, target+1):
#     if i%3 == 0 and i%5 != 0:
#         print("Fizz")
#     elif i%5 == 0 and i%3 != 0:
#         print("Buzz")
#     elif i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     else:
#         print(i)
#-------------------------------------------#


#-------------------------------------------#
# Project PyPassword
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_number = int(input("How many numbers would you like?\n"))

#===========================#
#Eazy Level
# hfaj^$25
# password = ""
# for i in range(nr_letters):
#     password += random.choice(letters)

# for i in range(nr_symbols):
#     password += random.choice(symbols)

# for i in range(nr_number):
#     password += random.choice(numbers)

# print(password)
#===========================#


#===========================#
# Hard Level
# g^2jk8$

# password_list = []
# for i in range(nr_letters):
#     password_list.append(random.choice(letters))

# for i in range(nr_symbols):
#     password_list.append(random.choice(symbols))

# for i in range(nr_number):
#     password_list.append(random.choice(numbers))

# # print(password_list)
# random.shuffle(password_list)
# password = ''.join(password_list)
# print(f"Your password is: {password}")
#===========================#


#===========================#
# password = ""
# total_password = [letters, numbers, symbols]
# total_word = nr_letters + nr_number + nr_symbols
# letters_count = numbers_count = symbols_count = 0 
# while True:
#     number = random.randint(0, 2)
#     if number == 0 and letters_count <= nr_letters:
#         letters_count += 1
#         password += random.choice(letters)
#     if number == 1 and numbers_count <= nr_number:
#         numbers_count += 1
#         password += random.choice(numbers)
#     if number == 2 and symbols_count <= nr_symbols:
#         symbols_count += 1
#         password += random.choice(symbols)
#     if len(password) == total_word:
#         break

# print(password)
#===========================#
#-------------------------------------------#
##########################################################################################
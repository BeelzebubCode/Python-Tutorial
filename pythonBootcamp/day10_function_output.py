# Functions with Outputs
'''
def my_function():
    result = 3 * 2
    return result
'''

# def format_name(f_name, l_name):
#     full_name = (f_name + " " + l_name).title()
#     return f"full name: {full_name}"

# format_fullname = format_name("AnGELA", "YU")
# print(format_fullname)
###########################################################################################


###########################################################################################
# Multiple return values
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     full_name = (f_name + " " + l_name).title()
#     return f"Full Name: {full_name}"

# format_fullname = format_name(input("What is your first name? "), input("What is your last name? "))
# print(format_fullname)

#----------------------------------------------------#
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
  
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#     if month == 2 and is_leap(year):
#         return 29
    
#     return month_days[month-1]

# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)
#----------------------------------------------------#
###########################################################################################


###########################################################################################
# Python เป็นที่รู้จักใน Docstrings
# Docstrings เป็นวิธีสร้างเอกสารเล็กน้อยในขณะที่เรากำลังเขียนโค้ดในฟังก์ชันของเราหรือในโค้ดอื่นๆ
# Docstring ต้องเป็นบรรทัดแรกของฟังก์ชันและใช้ """ ... """

# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#     to return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     full_name = (f_name + " " + l_name).title()
#     return f"Full Name: {full_name}"

# format_fullname = format_name(input("What is your first name? "), input("What is your last name? "))
# print(format_fullname)

# format_name
# ระหว่างจะเขียนจะเรียกฟังก์ชันจะแสดงข้อความที่เราเขียนอธิบายไว้(Docstrings)

# Project **Calculator
###########################################################################################

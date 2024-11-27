# def greet():
#     print("Hello Angela")
#     print("How do you do Angela?")
#     print("Isn't the weather nice today?")

# greet()
##############################################################################################


##############################################################################################
# Function with Input
# def my_function(something):
#     Do this with something
#     Then do this
#     Finally do this

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Angela")
#--------------------------------------#
# Function with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet_with("Jirat", "Thai")
# greet_with("Jack Bauer", "Nowhere")
#--------------------------------------#


#--------------------------------------#
# Function with keyword arguments
# greet_with(location="London", name="Angela")

#--------------------------------------#


#--------------------------------------#
# import math as m

# def paint_calc(height, width, cover):
#     cans = m.ceil((height*width) / cover)
#     print(f"You'll need {cans} cans of paint.")

# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#--------------------------------------#


#--------------------------------------#
# prime number
# def prime_checker(number):
#     is_prime = True
#     i = 2
#     while i < number:
#         if number % i == 0:
#             is_prime = False
#             print("It's not a prime number.")
#             break
#         i += 1
    
#     if is_prime:
#         print("It's a prime number.")

# n = int(input()) # Check this number
# prime_checker(number=n)
#--------------------------------------#

# **Caesar Cipher
##############################################################################################
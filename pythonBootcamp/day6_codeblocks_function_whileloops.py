# Function
# Defining Function
'''
def my_function():
    Do this
    Then do this
    Finally do this
'''
# function Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Use 4 spaces
# def my_function():
#     print("Hello")
#     print("Bye")
#     if True:
#         print("Hi")

# my_function()

#-----------------------------#
# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#      move()
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()
    
# for step in range(6):
#     jump()
#-----------------------------#
########################################################################


########################################################################
# While Loop

# while something_is_true:
#     Do something repeatedly

# def jump():
#     print("Jump!")

# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

#-----------------------------#
# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# while not(at_goal()):
#     jump()
#     print(at_goal())
#-----------------------------#


#-----------------------------#
# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear():
#         move()
#     if wall_in_front(): # or else
#         jump()
#-----------------------------#


#-----------------------------#
# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#=====================#
# def jump():
#     turn_right()
#     move()
#     turn_right()
#     move()
    
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     else:
#         jump()
#-----------------------------#


#-----------------------------#
# Reeborg's World
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()
     
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     else:
#         move()
#-----------------------------#
########################################################################
################################################################
# Random number
# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# # random 0.000000 - 0.9999999...
# random_float = random.random()
# print(random_float)

# h_or_t = random.randint(0, 1)
# if h_or_t == 1:
#     print("Heads")
# else:
#     print("Tails")
################################################################


################################################################
# List
# fruits = [item1, item2]

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
# "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",
# "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
# "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[1])
# states_of_america[1] = "Pencilvania";   print(states_of_america[1])
# states_of_america.append("Angelaland"); print(states_of_america)
# states_of_america.extend(["Angelaland", "Jack Bauer Land"])
# print(states_of_america)

#------------------------------------------------#
# Project random list
# import random
# names = input().split(", ")
# name = names[random.randint(0, len(names)-1)]
# print(name + " is going to buy the meal today!")
#------------------------------------------------#

# num_of_states = len(states_of_america)-1
# print(states_of_america[num_of_states])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozon = [fruits, vegetables]
# print(dirty_dozon)

# print(dirty_dozon[0])
# print(dirty_dozon[1])

# print(dirty_dozon[0][2])
# print(dirty_dozon[1][3])

#------------------------------------------------#
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
# position = list(position)
# position[1] = int(position[1])-1

# if position[0].upper() == "A":
#     map[position[1]][0] = "X"
# elif position[0].upper() == "B":
#     map[position[1]][1] = "X"
# elif position[0].upper() == "C":
#     map[position[1]][2] = "X"
###################################
# letter = position[0].lower()
# abc = ["a","b","c"]
# letter_index = abc.index(letter)
# number_index = int(position[1])-1
# map[number_index][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")
#------------------------------------------------#


#------------------------------------------------#
# Game rock paper scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if chose >= 3 or chose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game[chose])
    print("Computer chose:")
    computer_chose = random.randint(0, 2)
    print(game[computer_chose])

    if chose == computer_chose:
        print("It's a draw")
    else:
        if (chose == 0 and computer_chose == 1) or (chose == 1 and computer_chose == 2) or (chose == 2 and computer_chose == 0):
            print("You lose")
        else:
            print("You win")
#------------------------------------------------#
################################################################
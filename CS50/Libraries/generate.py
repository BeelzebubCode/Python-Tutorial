# # import random
# from random import choice

# # coin = random.choice(["heade", "tails"])
# coin = choice(["heade", "tails"])
# print(coin)
#######################################################################


#######################################################################
# import random

# #random.randint(A, B) จะได้ค่า A - B
# number = random.randint(1, 10)
# print(number)
#######################################################################


#######################################################################
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card, end=" ")
#######################################################################
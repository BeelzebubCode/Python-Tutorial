############################################################################################################
# # ทำเองครั้งแรก 
# from random import randint
# from game_data import data
# from art import logo, vs
# from replit import clear

# game_should_continue = False
# score = 0
# account_a = get_random_account()
# print(logo)
# while not game_should_continue:     
#     while True:
#         account_b = get_random_account()
#         if account_a != account_b:
#             break
#     print(f"Compare A: {account_a["name"]}, a {account_a["description"]}, from {account_a["country"]}")
#     print(vs)
#     print(f"Against B: {account_b["name"]}, a {account_b["description"]}, from {account_b["country"]}")

#     followers_A = account_a["follower_count"]
#     followers_B = account_b["follower_count"]
#     if followers_A > followers_B:
#         result = 'A'
#     elif followers_A < followers_B:
#         result = 'B'
#         account_a = account_b

#     choose = input("Who has more followers? Type 'A' or 'B': ").upper()
#     clear()
#     print(logo)
#     if choose == result:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     else:
#         game_should_continue = True
#         print(f"Sorry, that's wrong. Final score: {score}")
############################################################################################################


############################################################################################################
# ปรับปรุง
from random import randint
from game_data import data
from art import logo, vs
from replit import clear

def get_random_account():
    """Get data from random account"""
    return data[randint(0, len(data)-1)]

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()

    # Make the game repeatable
    while game_should_continue:     
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(guess, a_followers, b_followers)

        if  guess == "b" and is_correct:
            account_a = account_b

        clear()
        print(logo)
        # Give user feedback on their guess.
        # Score keeping
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
############################################################################################################
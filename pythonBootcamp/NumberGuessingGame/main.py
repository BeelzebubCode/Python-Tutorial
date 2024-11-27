from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_number_guess(guess_number, number, health):
    """ checks answer against guess. Returns the number of health remain """
    if guess_number < number:
        print("Too low.")
        return health - 1
    elif guess_number > number:
        print("Too high.")
        return health - 1
    else:
        print(f"You got it! The answer was {number}.")
    
def set_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choose == 'easy':
        return EASY_LEVEL_TURNS
    elif choose == 'hard':
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    health = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {health} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        health = check_number_guess(guess, answer, health)

        if health == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
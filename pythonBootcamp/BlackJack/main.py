from replit import clear
from art import logo
import random

def draw_card(amount):
    """ Return a random card from the deck. """
    new_card = []
    for _ in range(amount):
        new_card.append(random.choice(cards))
    
    return new_card

# คำนวน score โดยรับ cards มา
def calculator_score(in_cards):
    """ Take a list of cards and return the score calculated from the cards """
    # ถ้าไพ่เราได้ 21 โดยมีแค่ 2 ใบ = blackJack
    if sum(in_cards) == 21 and len(in_cards) == 2:
        return 0
    
    # A สามารถเป็น 11 or 1 ได้
    # ถ้าเราได้ A แล้วมันนำมาบวกเกิน 21  จะให้ A = 1
    if 11 in in_cards and sum(in_cards) > 21:
        in_cards.remove(11)
        in_cards.append(1)

    return sum(in_cards) # ส่งผลรวมออกไป

# คำนวณว่าใครชนะ
def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw 😑"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > computer_score:
        return "You win 😊"
    else:
        return "You lose 😤"

# ไพ่ทั้งหมด
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play_game():
    print(logo)
    player_cards = draw_card(2)
    computer_cards = draw_card(2)

    is_game_over = False
    # loop เราจั่วไพ่
    while not is_game_over:
        # Data of player and computer
        player_score = calculator_score(player_cards)
        computer_score = calculator_score(computer_cards)
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        # ถ้าเราได้ blackjact หรือ com ได้จะให้หยุดการจั่วไพ่ หรือเราจั่วได้เกิน 21 แต้ม
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            is_draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if is_draw_card == 'y': # จั่วไพ่ต่อ
                player_cards += draw_card(1)
            else:
                # จบการจั่วไพ่
                is_game_over = True

    # ให้คอมจั่วไพ่
    while computer_score != 0 and computer_score < 17:
        computer_cards += draw_card(1)
        computer_score = calculator_score(computer_cards)

    print(f"    You final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score)) # คำนวณว่าใครชนะ

# จะเล่นเกมต่อหรือไม่
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()
    play_game() 
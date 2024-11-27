#--------------------------------------#
# from pyfiglet import Figlet
# from replit import clear
from art import logo

# def render(text, style):
#     f = Figlet(font=style)
#     print(f.renderText(text))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         cipher_text += alphabet[alphabet.index(letter)+shift_amount]
#         # position = alphabet.index(letter)
#         # new_position = position + shift_amount
#         # new_letter = alphabet[new_position]
#         # cipher_text += new_letter
    
#     print(f"The encoded text is = {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         # print(alphabet.index(letter))
#         plain_text += alphabet[alphabet.index(letter)-shift_amount]

#     print(f"The decrypt text is = {plain_text}")

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    # print(shift_amount)

    end_text = ""
    for letter in start_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    
    print(f"The {cipher_direction}d is = {end_text}")
    
print(logo)
# render("caesar cipher", "univers")

end_of_code = False
while not end_of_code:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    option = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if option == 'no':
        end_of_code = True
        print("Goodbye")
#--------------------------------------#
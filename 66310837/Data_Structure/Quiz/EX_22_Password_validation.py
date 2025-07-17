# import re

# def validate_password(password):

#     if len(password) < 6 or len(password) > 12:
#         return False

#     if not re.search('[a-z]', password):
#         return False
    
#     if not re.search('[A-Z]', password):
#         return False
    
#     if not re.search('[0-9]', password):
#         return False
    
#     if not re.search('[#$@]', password):
#         return False
    
#     return True

# def check_password(passwords):
#     valid_password = [pwd for pwd in passwords if validate_password(pwd)]
#     return ','.join(valid_password)

# password_list = input().split(',')
# passwords = check_password(password_list)
# print(passwords)
######################################################################################


def check_password(pw_list):
    passwords = []
    for pw in pw_list:
        if all([check_str_length(pw), check_str_low(pw), check_str_up(pw), check_str_character(pw), check_str_number(pw), check_str_null(pw)]):
            passwords.append(pw)
    return passwords

def check_str_low(pw):
    for char in pw:
        if char.islower():
            return True
    return False

def check_str_up(pw):
    for char in pw:
        if char.isupper():
            return True
    return False

def check_str_character(pw):
    character = set('#$@')
    return bool(character & set(pw))
    
def check_str_number(pw):
    number = set('1234567890')
    return bool(number & set(pw))

        
def check_str_length(pw):
    return 6 <= len(pw) <= 12
    # if len(pw) >= 6 and len(pw) <= 12:
    #     return True
    # else:
    #     return False

def check_str_null(pw):
    if " " in pw:
        return False
    return True

password_list = input().split(',')
passwords = check_password(password_list)
print(','.join(passwords))
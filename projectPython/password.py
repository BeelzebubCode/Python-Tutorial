import random
import string

def numbers_passWord(numbers) :
    passwords=[]
    for i in range(numbers) :
        if i %3 == 0 :
            i = random.choice(string.ascii_uppercase)
            passwords.append(i)
        elif i %5 == 0:
            i = random.choice(string.ascii_lowercase)
            passwords.append(i)
        else :
            i = str(random.randint(0,9))
            passwords.append(i)
    return passwords


number=int(input("ต้องการรหัสที่มีความยาวเท่าไหร่ : "))
passWords=numbers_passWord(number)

print("รหัสผ่านของคุณ :",''.join(passWords))

str = input().lower()
check = input()

newStr = str.split(check)
checkParn = ''.join(newStr)

# print(newStr)
# print(checkParn)
if(checkParn == checkParn[::-1] and checkParn != ''):
    print(True)
else:
    print(False)

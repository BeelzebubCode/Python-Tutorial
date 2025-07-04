n = int(input())
chack = True

for i in range(2, n):
    if n%i == 0:
        chack = False
        break

if chack and n>1:
    print("Prime")
else:
    print("Not Prime")
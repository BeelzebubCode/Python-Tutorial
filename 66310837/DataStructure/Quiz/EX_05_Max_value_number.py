number = input().split()

if len(number) <= 5:
    number = [int(i) for i in number]
    print(max(number))
else:
    print("Too much input!")
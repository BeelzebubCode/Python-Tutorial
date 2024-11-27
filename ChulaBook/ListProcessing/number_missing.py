number = input()

number_missing = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in number:
    if num in number_missing:
        number_missing.remove(num)

if number_missing:
    print(','.join(number_missing))
else:
    print(None)
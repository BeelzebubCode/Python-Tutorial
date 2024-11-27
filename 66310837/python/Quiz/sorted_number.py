number = sorted(list(map(int, input().split())), reverse=True)
# reverse = True ทำให้เรียงจากมากไปน้อย

# number = input().split()
# number = list(map(int, number))
# number = sorted(number, reverse=True)

if len(number) < 5:
    print("Too few input")
else:
    # print() 3  index แรกมาเลยเนื่องจาก sorted มาก->น้อย แล้ว
    for i in range(3):
        print(number[i], end=" ")

loop = int(input())

if loop == 0:
    print(f"{0:.2f}")
else:
    numbers = [float(input()) for _ in range(loop)]
    numbers.sort()

    result = loop // 2

    if loop % 2 != 0:
        print(f"{numbers[result]:.2f}")
    else:
        M = (numbers[result-1]+numbers[result])/2
        print(f"{M:.2f}")
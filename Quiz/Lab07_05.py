def three_digits_to_word(n):
    unit_list = ["zero", "one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_list = ["", "", "twenty", "thirty", "forty", "fifty",
             "sixty", "seventy", "eighty", "ninety"]
    
    if n <= 19 and n >= 0:
        return unit_list[n]
    elif n > 20 and n <= 99:
        numList = [int(i) for i in str(n)]
        return f' {tens_list[numList[0]]}-{unit_list[numList[1]]}'
    elif n > 99 and n < 1000:
        newStr = str(n)
        return f'{unit_list[int(newStr[0])]} hundred {three_digits_to_word(int(newStr[1:]))}'

number = int(input('Enter a number: '))
result = three_digits_to_word(number)
print(result)
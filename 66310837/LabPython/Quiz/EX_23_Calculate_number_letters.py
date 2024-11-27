str = input().replace(" ", "")

letters_count = digits_count = 0
for char in str:
    if char.isalpha():
        letters_count += 1
    elif char.isnumeric():
        digits_count += 1

print("LETTERS", letters_count)
print("DIGITS", digits_count)
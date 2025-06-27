word = input().lower()
palindrome_word = word[::-1]

print("Yes" if word == palindrome_word else "No")
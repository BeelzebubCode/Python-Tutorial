import sys

word = sys.stdin.readline().strip().lower()
word = sorted(word)

word_char = {}
for i in word:
    if i not in word_char:
        word_char[i] = 1
    else:
        word_char[i] += 1

if " " in word:
    del word_char[" "]

print(word_char.items())
for k, v in word_char.items():
    print(f"{k}: {v}")


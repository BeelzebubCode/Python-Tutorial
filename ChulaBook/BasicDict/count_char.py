data = input().lower()
count_char = {}

for char in data:
    if char not in count_char:
        count_char[char] = 1
    else:
        count_char[char] += 1

# sorted_count = sorted(count_char.items(), key=lambda item: item[1], reverse=True)
sorted_count = sorted([(count, char) for char, count in count_char.items()], key=lambda item: (-item[0], item[1]))
# print(sorted_count)
for count, char in sorted_count:
    print(char, "->", count)
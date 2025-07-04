word = input().lower()

ls = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in ls:
    count += word.count(i)

print(count)
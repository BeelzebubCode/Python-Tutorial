str = input().lower()

new_str = []

for i in str:
    if i not in new_str:
        new_str.append(i)
new_str = sorted(new_str)

print(''.join(new_str))
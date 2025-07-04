max_number = 0

for i in range(3):
    n = int(input())
    if max_number < n:
        max_number = n
    
print(max_number)
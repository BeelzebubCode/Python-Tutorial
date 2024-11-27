n = int(input())

square = ""
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            square += "*"
        else:
            square += " "
    square += "\n"
print(square)

square = []
for i in range(n):
    row = []
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            row.append("*")
        else:
            row.append(" ")
    square.append(row)
    
for row in square:
    print(''.join(row))
# n = int(input())

# space = int(n/2)
# for i in range(space, 0, -1):
#     print(' '*(space-i)+'*'+' '*(i*2-1)+'*')

# print(' '*space+'*')
# for i in range(1, space+1):
#     print(' '*(space-i)+'*'+' '*(i*2-1)+'*')
#######################################################

# for i in range(n):
#     for j in range(n):
#         if j == i or i + j == n-1:
#             print("*", end="")
#         else: 
#             print(" ", end="")
#     print()

n = int(input())

for i in range(n):
    l = []
    for j in range(n):
        l.append(" ")

    l[i] = "*"
    l[-(i+1)] = "*"
    print("".join(l))
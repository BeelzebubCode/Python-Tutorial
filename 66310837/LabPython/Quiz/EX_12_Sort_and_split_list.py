# input_str = input().split(';')

# num = [group.split(',') for group in input_str]
# result = []

# try:
#     for i in range(len(num)):
#         for j in range(len(num[i])):
#             try:
#                 num[i][j] = int(num[i][j])
#             except ValueError:
#                 raise TypeError("Input Error: Non-numeric value encountered")
            
#     num.sort()
#     for i in range(len(num)):
#         for j in range(min(num[i]), max(num[i])):
#             result.append([j, j+1])
    
#     print(result)
# except TypeError as e:
#     print(e)
#########################################################

input_str = input().split(';')

num = [group.split(',') for group in input_str]
num = list(map(lambda n : list(map(int, n)), num))
result = []

num.sort()
for i in range(len(num)):
    for j in range(min(num[i]), max(num[i])):
        result.append([j, j+1])

print(result)

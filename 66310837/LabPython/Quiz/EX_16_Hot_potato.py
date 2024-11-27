# str = input().split(';')
# name_list, number = str[0].split(','), int(str[1])

# stack = []
# count = 0
# while name_list:
#     for i in range(1, number+1):
#         # print(i, count)
#         if i == number:
#             stack.append(name_list.pop(count))
#             count -= 1
#             # print(stack)
#             # print(name_list)

#         count += 1
#         if count > len(name_list)-1:
#             count = 0 

# for name in stack:
#     print(name)



# kuy = input().split(";")
# kuy1 = kuy[0].split(",")
# kuy2 = int(kuy[1])

# queue = []
# for name in kuy1:
#     queue.insert(0, name)

# while queue != []:
#     for _ in range(kuy2-1):
#         queue.insert(0, queue.pop())
#         print(queue)
#     print(queue.pop())
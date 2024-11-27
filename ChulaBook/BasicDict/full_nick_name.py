def reverse(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict

n = int(input())
dict_name = {}
for _ in range(n):
    data = input().split()
    dict_name[data[0]] = data[1]

m = int(input())
data_m = []
for _ in range(m):
    name = input()
    data_m.append(name)

print("+==============+")
reverse_dict_name = reverse(dict_name)
for item in data_m:
    if item in dict_name:
        print(dict_name[item])
    elif item in reverse_dict_name:
        print(reverse_dict_name[item])
    else:
        print("Not found")

"""
input:
10
Robert Dick
William Bill
James Jim
John Jack
Margaret Peggy
Edward Ed
Sarah Sally
Andrew Andy
Anthony Tony
Deborah Debbie
4
John
Jim
Don
Debbie

Output:
Jack
James
Not found
Deborah
"""
n = int(input())

name_data = [
    "Robert",
    "William",
    "James",
    "John",
    "Margaret",
    "Edward",
    "Sarah",
    "Andrew",
    "Anthony",
    "Deborah"
]

nick_name_data = [
    "Dick",
    "Bill",
    "Jim",
    "Jack",
    "Peggy",
    "Ed",
    "Sally",
    "Andy",
    "Tony",
    "Debbie"
]

check_name = []
for _ in range(n):
    name = input()
    check_name.append(name)

for name in check_name:
    if name in name_data:
        print(nick_name_data[name_data.index(name)])
    elif name in nick_name_data:
        print(name_data[nick_name_data.index(name)])
    else:
        print("Not found")
def reverse(d):
    # print(type(d))
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key
    return new_dict

def keys(d, v):
    list_data = []
    for key in d:
        if v == d[key]:
            list_data.append(key)
    return list_data


print(reverse({3: "A", 2: "B"}) == {"A": 3, "B": 2})
print(keys({3: 33, 4: 33, 5: 55, 2: 33}, 33))
print(keys({3: 33, 4: 33, 5: 55, 2: 33}, 9999))
import json

# file_data = open('data.json')
# data = json.load(file_data)

# for item in data:
#     print(data[item])

# file_data.close()
####################################################

# with open('data.json') as file:
#     data = json.load(file)

# for key in data:
#     print(f"{key} : {data[key]}")
#####################################################
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)
# map(function, iterables)

# def addition(n):
#     return n + n

# numbers = [1, 2, 3, 4]
# result = map(addition, numbers)

# print(result)

# # แปลง map ให้เป็น list เพื่อง่ายต่อการอ่าน
# print(list(result))

def myfunc(a):
    return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
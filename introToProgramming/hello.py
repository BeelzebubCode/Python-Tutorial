print("Hello World!")
print('Tou should try.')

# string
print("50/2")
# number 
print(50/2)

# print("Jirat",end=" ")
# print("Fongda")
# print("age: 20")

# print(bool(-1), bool(0), bool("Love"))
# print("2"+"3")
# print("A"*5)
# print(5/2)
# print(5//2)
# print(10**3)

x = 0
x+=10 # x = x + 10
print(x)
print((-2)**4)

name = "John"
surname = "Doe"
print("My name is",name,".","My last name is",surname)

print("Hello", end=",")
print("hi")

A = "X"
A+="A"
A+="A"
print("result =", 3*A)
# XAAXAAXAA

x = 5
print("result =", str(x)*int(x))

# %d integer
# %f float
# %s string
x, y, z = 16, 26.42, 7.56
print("x = %d, y = %.1f, z = %.3f" % (x, y, z))

# format
text = "My name is {fname}, I'm {age}"
print(text.format(fname = "John", age = 18))
print("My name is {0}, I'm {1}".format("John",25))
print("Money {:,}".format(1900000))

# input output
# x = input("What's you name?: ")
# print("Nice to meet you,", x)

# a, b, c, = input("Give me three names: ").split()
# print(a, b, c)

# a, b, c = input("gimme 3 numbers: ").split()
# a, b, c = int(a), int(b), int(c)
# average = (a+b+c)/3
# print("Average of", a, b, c, "is ", average)

a, b, c = map(int, input("gimme 3 numbers: ").split())
average = (a+b+c)/3
print("Average of", a, b, c, "is ", average)

# ใช้ split กำหนดตัวคันได้
a, b, c = input("Input: ").split("x")
print("a =", a)
print("b =", b)
print("c =", c)

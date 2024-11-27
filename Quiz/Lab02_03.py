
m1 = (float)(input("m1: "))
b1 = (float)(input("b1: "))
m2 = (float)(input("m2: "))
b2 = (float)(input("b2: "))

x = (b2-b1)/(m1-m2)
y = m1*x+(b1)
print(f'Lines intersect at ({x:.2f},{y:.2f})')
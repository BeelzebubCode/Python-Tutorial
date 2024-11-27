import math

def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon=10**-6):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)

    if abs(distance - (r1+r2)) < epsilon:
        return 0
    elif distance < r1+r2:
        return 1
    else:
        return -1


x1, y1, r1 = map(float, input().split(' '))
x2, y2, r2 = map(float, input().split(' '))

print(circle_intersect(x1, y1, r1, x2, y2, r2))

# num1 = [int(i) for i in circle1.split(' ')]
# num2 = [int(i) for i in circle2.split(' ')]
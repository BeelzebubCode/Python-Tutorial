from math import factorial as f

# print(f(10)/(f(3)*f(3)*f(2)))
# print(f(8)/f(5))
# print(f(11)/(f(4)*f(4)*f(2)))
# print(f(10)/(f(3)*7))
# print(f(9))

# 5! / (5-3)!3!

x = f(12)/(f(12-2)*f(2))
y = f(5)/((f(5-3)*f(3)))
print(x*y)
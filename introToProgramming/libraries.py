import math
# print(math.pi)

# import math as m
# print(m.cos(m.pi))

# from math import *
# print(cos(pi))

# แบบนี้ต้องระวังชื่อซ้ำกันอันอื่น อะไรที่ import หลังจะไปทับอันก่อนหน้า
# from math import *
# from cmath import * # ทับ math
# print("cosine of pi =", cos(pi))

# print(math.ceil(3.1)) #ปัดขึ้นหมด
# print(math.floor(3.9)) #ปัดลงหมด
# print(math.fabs(-3)) #ทำเป็นบวกและคืนเป็นทศนิยม
# print(math.factorial(4)) #ค่า factorial ห้ามใส่ลบ error
# print(math.exp(10)) #e^10
# print(math.log(10, 10)) #(log10,  base10)
# print(math.pow(5, 2)) #5^2
# print(math.sqrt(2)) #root

# math.acos(radians) math.asin math.atan
# math.cos math.sin math.tan
# ข้างบนนี้ใช้หน่วย radians
# math.degrees() แปลง radians เป็นองศา
# math.radians() แปลง degrees เป็นเรเดียน
# print(math.cos(math.radians(30)))

# print(math.pi)
# print(math.e)

# a = math.sin(math.radians(30))
# print("%.2f" % a)
# a = math.sin(math.pi) + math.cos(math.pi)
# print("%.2f" % a)

# print(round(3.56)) #ปัดตามปกติที่ใช้กันทั่วไป
# print(round(3.56, 1)) # ใส่ 1 คือต้องการปัดให้เหลือทศนิยม 1 ตำแหน่ง

####################################
# A = absin(c)/2
# a, b = input("Enter lengths of two sides: ").split(" ")
# a, b = int(a), int(b) #ควรเป็น float

# c = int(input("Enter an angle between them: ")) #ควรเป็น float
# c = math.sin(math.radians(c)) 
# print("The area of the triangle is {result}".format(result = a*b*c/2))

####################################
# A = pi*r(root h^2 + r^2) + pi*r^2
# r = 1.0
# h = 2.0
# A = math.pi*r*math.sqrt(h**2+r**2) + math.pi*r**2
# print(A)
#########################################################################

#########################################################################
#========================#
#   random
# =======================#
# import random 
import random as r

# print(r.randint(0, 9)) # สุ่มเลข 0-9
# print(r.random()) # สุ่มตัวเลขต้องแต่ช่วง 0-1 || 0.0-0.9999 อาจไม่ถึง 1

# choice(seq) ใส่ชุดข้อมูล
# print(r.choice([2, 3, 5, 7])) #สุ่มข้อมูลมาจากชุดข้อมูล 1 ค่า

# number = [1, 2, 3]
# r.shuffle(number) #สลับค่าในชุดข้อมูล
# print(number)

# OTP 6 หลัก
# otp = r.randint(0, 999999)
# print("%06d" % otp)

# OTP n หลัก
# n = int(input())
# otp = r.randint(0, 10**n-1)

# print("%0*d" % (n,otp))
#########################################################################


#########################################################################
#========================#
#   String methods
# =======================#
# str = "hello"
# print(str.capitalize()) #แปลงตัวแรกให้เป็นพิมพ์ใหญ่
# print(str.lower()) #แปลงเป็นพิมพ์เล็ก
# print(str.upper()) #แปลงเป็นพิมพ์ใหญ่

#############################
# str ที่เราเอามามีคุณสมบัตินี้ไหม
# print("hello".isalpha()) #alphabets (A-Za-z)
# print("covid19".isalpha())

# print("1234".isnumeric()) #เป็นตัวเลขหรือป่าว
# print("3.14".isnumeric()) #ถูกมองไม่เป็นตัวเลขเพราะจุด ( . )
# print("hello".isnumeric())
# print("covid19".isnumeric())

# print(" ".isspace()) #ตรวจสอบว่าเป็น space ทั้งหมดไหม ("  ")
# print(" 12".isspace())
# print("HELLO".isupper()) #ตรวจสอบว่าเป็นตัวใหญ่ทั้งหมดไหม
# print("COVID19".isupper()) #ไม่สนใจตัวเลข
# print("Covid19".isupper())
# print("JI RAT FONG DA".split(" ")) #แบ่งข้อความออกตามแบบที่เรากำหนด default " "

# d = 8764521
# print(d.isnumeric()) # error เอา number มาเรียก method ของ str ไม่ได้
#########################################################################

###############################################################
#               installing new libraries                      #
# Windows => py -2 -m pip install [library name]              #
# pip install [library name] | not version python             #  
# macOS and Linux => pip3 install -user [library name]        #
###############################################################

#########################################################################
#   NumPy 
# เป็นทีเด็ดของ python จัดการพวกตัวเลขถูกพูดถึงตลอดเมื่อทำงานกับข้อมูล
# math ทำงานกับเลขเดียว แต่ numpy เราสารารถโยนชุดตัวเลขให้มันได้เลย
import numpy as np

# # เซ็ตให้ print ทกศนิยม 2 แหน่งแบบ fixed เลย
# np.set_printoptions(precision=2, floatmode="fixed")

# # numpy.arange(start, stop, step)
# print(np.arange(0, 10, 2)) #สร้างก่อนถึง step ต้องระวังเรื่องนี้มีหลายฟังช์ชั่นใน python
# print(np.arange(0, 2, 0.5))
# # print(np.arange(1, 10, 0.1))

# v = np.arange(0, 1, 0.2)
# print(v)
# print(v+2)
# print(np.power(v, 2))
# print(np.exp(v))
#########################################################################

#########################################################################
#   Matplotlib
import matplotlib.pyplot as plt
# ความหมาย import แบบนี้คือ เรานำ pyplot มาใช้ซึ่งมันอยู่ใน matplotlib ซึ่งมขนาดใหญ่มากๆ

# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# plt.plot(x, y)  #ตั้งค่าแกน x, y
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('Simple Plot')
# plt.show()

# x = np.arange(-10, 10, 0.1)
# y = x**2 + 2*x + 1

# plt.plot(x, y, color="blue", linewidth=2, linestyle="dotted")
# plt.show()
#plt.savefig("file name.png")

# plt.plot(x, y, color="blue", linewidth=2)
# plt.xlim(0, 5)
# plt.ylim(0, 40)
# plt.show()

# วาดกราฟมากกว่า 1 กราฟ
# x = np.arange(-math.pi*2, math.pi*2, 0.1)
# y1 = np.cos(x)
# y2 = np.sin(x)

# plt.plot(x, y1, color="blue", linewidth=2, linestyle="dashed")
# plt.plot(x, y2, color="orange", linewidth=2)
# plt.xlim(-20, 20)
# plt.show()

# f(x) = (x^2(x+1))^1/2
# x = np.arange(1.0, 10.0, 0.1)
# y = np.sqrt(np.pow(x, 2)*(x+1))


# plt.plot(x, y, color="red", linewidth=2)
# plt.show()


# f(x) = 7-4x x<1
#        x^2+2 x>=1
x = np.arange(-5, 6, 1)
y1 = 7-4*x
y2 = np.pow(x, 2)+2

plt.plot(x, y1, color="red", linewidth=2)
plt.plot(x, y2, color="blue", linewidth=2)
plt.xlim(-5, 5)
plt.show()

# print(x)
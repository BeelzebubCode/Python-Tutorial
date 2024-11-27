"""
ความสัมพันธ์เวียนเกิด(Recursion) คือ
    *วิธีแก้ปัญหาด้วยการแตกเป็นปัญหาย่อยๆจนถึงส่วนที่ย่อยที่สุด
    *มักจะเป็นฟังก์ชั่นที่เรียกตัวเอง
"""
################################################################
# วิธีใช้ loop
# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum += i
#     return theSum

# print(listsum([1,3,5,7,9]))
"""
0 + 1 = 1
1 + 3 = 4
4 + 5 = 9
9 + 7 = 16
16 + 9 = 25

((((1+3)+5)+7)+9)
จัดรูปใหม่
(1+(3+(5+(7+9))))   total = (1+(3+(5+(7+9))))
(3+(5+(7+9)))       total = (1+(3+(5+16)))
(5+(7+9))           total = (1+(3+21))
(7+9)               total = (1+24)
9                   total = 25
"""
# แปลงเป็นโปรแกรม
# def listsum(numList):
#     if len(numList) == 1:
#         return numList[0]
#     else:
#         return numList[0] + listsum(numList[1:])

# print(listsum([1, 3, 5, 7, 9]))

"""
==================================
การทำงาน
sum(1,3,5,7,9)  = 1+
sum(3,5,7,9)    = 3+
sum(5,7,9)      = 5+
sum(7,9)        = 7+
sum(9)          = 9

(1+(3+(5+(7+9))))
9+7 -> 5+16 -> 3+21 -> 1+24 = 25
==================================
กฎของความสัมพันธ์เวียนเกิด(Recursion)
    *ต้องมีกรณีฐาน
    *ต้องเปลี่ยนสถานะเข้าสู่กรณีพื้นฐาน
    *ต้องเรียกตัวเอง

def listsum(numList):
    if len(numList) == 1: **กรณีฐาน
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:]) ⬇️

**listsum() เรียกตัวเอง
**listsum(numList[1:] ->>> เปลี่ยนสถานะ )
"""
################################################################


################################################################
# ฝึก recursion function
# def tri_recursion(k):
#     if k > 0:
#         result = k + tri_recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("Recursion Example Results")
# tri_recursion(6)
#========================================#


#========================================#
# factorial
# def factorial(numeric):
#     if numeric != 0:
#         return numeric * factorial(numeric-1)
#         # print(result)
#     else:
#         return 1

# num = int(input("Input numeric: "))
# result = factorial(num)
# print(f"The factorial of {num}! is {result}")
#========================================#


#========================================#
# เลขฐาน
# def toStr(number, base):
#     number_16 = "0123456789ABCDEF"
#     if number < base:
#         return number_16[number]
#     else:
#         return toStr(number//base, base) + number_16[number%base]
    
# number, number_base = input().split()
# number, number_base = int(number), int(number_base)
# print(toStr(number, number_base))
################################################################

# def fac(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac(n-1)

# print(fac(5))


hour = 3
n = 5

def recurren_hour(n, hour):
    if hour == 1:
        return n
    return 2 * recurren_hour(n, hour - 1)

print(recurren_hour(n, hour))
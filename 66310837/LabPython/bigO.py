# Big O
"""
Big O คือ 
    *ตัววัดประสิทธิภาพการทำงาน
    *วัดตามจำนวนข้อมูล n
"""
n = 10
thesum = 0
for i in range(1, n + 1):
    thesum = thesum + i
print(thesum)

"""
* ตัวอย่าง sum of n
    -จำนวน step ในการทำงาน T(n) = 2 + n
    -O(n)
    -ดูตัวที่ยกกำลังเยอะสุด
* T(n) = 5n^2 + 3n
    -O(n^2)
    -ดูตัวที่ยกกำลังเยอะสุดและไม่ต้องดูสัมประสิทธิ์
"""

#----------------------------------------#
# Big O = 1 or O(1)
# มี input เข้ามาแล้วออกเลย ทำครั้งเดียว
def evenOrOdd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

evenOrOdd(0)
evenOrOdd(9999999)
#----------------------------------------#


#----------------------------------------#
# Big O = n or O(n)
# n = จำนวนข้อมูลที่นำเข้า
# ถ้ามีข้อมูล 100 ตัวจะทำ 100 ครั้ง big O = O(n)

# def searchNumber(arr, value):
#     for i in range(len(arr)):
#         if(arr[i] == value):
#             return i
        
# numArray = [7, 16, 2, 0, 5, 1, 30]
# number = 30

# result = searchNumber(numArray, number)
# print(result)
#----------------------------------------#


#----------------------------------------#
# Big O = O(n^2)
# ใส่ input 2 ค่า Big O = O(2^2)

def duplicateCheck(arr):
    for i in range(len(arr)):
        a = arr[i]
        for j in range(i+1, len(arr)):
            b = arr[j]
            print(a, b)
            if(a == b):
                return "duplicated"
    return "not duplicate"

numArray = [1, 3, 5, 9]
result = duplicateCheck(numArray)
print(result)
# ในฟังก์ชั้นนี้ต่อให้เราใส่ไปแค่ 2 ค่าแต่มันมีการทำงานซ้อนข้างในอีก
# เช่น loop ซ้อน loop ทำลูปนอก เข้าลูปในทำในเสร็จออกไปวนนอกต่อ
#----------------------------------------#
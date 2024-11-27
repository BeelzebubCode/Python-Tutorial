# การค้นหาข้อมูล
# def sequentialSearch(alist, item):
#     pos = 0
#     found = False

#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos += 1

#     return found

# testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequentialSearch(testlist, 3))
# print(sequentialSearch(testlist, 13))


# การค้นหาข้อมูลที่มีการเรียงลำดับ 
# def orderedSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False

#     while pos < len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 # ให้หยุดเมื่อข้อมูลใน list มากกว่าค่าที่ค้นหา
#                 stop = True
#             else:
#                 pos += 1
#     return found

# testlist = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(orderedSequentialSearch(testlist, 5))
# print(orderedSequentialSearch(testlist, 31))

# การค้นหาแบบแบ่งครึ่ง binary search ( o log n )
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False

#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1
#     return found

# testlist = [17, 20, 26, 31, 44, 54, 56, 65, 77, 93]
# print(binarySearch(testlist, 55))
# print(binarySearch(testlist, 44))

# การค้นหาแบบแบ่งครึ่ง แก้ปัญหาแบบเวียนเกิด
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else: 
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

testlist = [17, 20, 26, 31, 44, 54, 56, 65, 77, 93]
print(binarySearch(testlist, 99))
print(binarySearch(testlist, 54))
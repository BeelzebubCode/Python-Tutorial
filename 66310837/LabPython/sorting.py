# Bubble sort
# เปรียบเทียบเป็นคู่ๆ **ช้า

# def bubbleSort(alist):
#     for passnum in range(len(alist)-1, 0, -1):
#         for i in range(passnum):
#             if alist[i] > alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubbleSort(alist)
# print(alist)

# count = 0
# list_number = [ 29, 23, 75, 39, 64, 67, 87, 94, 14, 48, 10, 87, 0, 20, 74, 17]
# for number in range(len(list_number)-1, 0, -1):
#     for i in range(number):
#         count += 1
#         if list_number[i] > list_number[i+1]:
#             temp = list_number[i]
#             list_number[i] = list_number[i+1]
#             list_number[i+1] = temp

# print(list_number)
# print(count)
################################################################


################################################################
# Short bubble sort
# def shortBubleSort(alist):
#     exchanges = True
#     passnum = len(alist)-1
#     while passnum > 0 and exchanges:
#         exchanges = False
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 exchanges = True
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#         passnum-=1

# alist = [20, 30, 40, 90, 99, 60, 70, 80, 100, 110]
# shortBubleSort(alist)
# print(alist)
################################################################


################################################################
# Selection sort
# หาตัวที่มากสุดไปวางที่ตำแหน่งสุดท้าย
# ใช้ n - 1 รอบในการเรียงลำดับ n ตัว
# def selectionSort(alist):
#     for fillslot in range(len(alist)-1, 0, -1):
#         positionMax = 0
#         for location in range(1, fillslot+1):
#             if alist[location]>alist[positionMax]:
#                 positionMax = location
        
#         temp = alist[fillslot]
#         alist[fillslot] = alist[positionMax]
#         alist[positionMax] = temp

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# selectionSort(alist)
# print(alist)
################################################################


################################################################
# Insertion sort
# ให้ตัวที่เรียงลำดับแล้วอยู่ด้านหน้า เริ่มที่ 1 ตัว
# ตัวถัดไปจะถูกใส่ในส่วนด้านหน้าให้ถูกตำแหน่ง

def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1] # เลื่อนไปทางขวา
            position = position - 1

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)
################################################################


################################################################
# Merge sort
# แบ่งเป็นปัญหาย่อยลงไปเรื่อยๆ
# รวมกลับขึ้นมาเป็นการแก้ปัญหาใหญ่ -เปรียบเทียบแล้วเลื่อนหมุด
################################################################




# data_str = input().split()

# # def get_str(data):
# #     for char in data:
# #         if char.isalpha():
# #             return char
# #     return ""

# # print(data_str)
# # print(sorted(data_str, key=get_str))

# # sorted_data = sorted(data_str, key=lambda data : [char for char in data if char.isalpha()])
# # print(sorted_data[0], sorted_data[len(data_str)//2], sorted_data[len(data_str)-1])

# sorted_data = sorted(data_str)
# print(sorted_data[0], sorted_data[len(data_str)//2], sorted_data[len(data_str)-1])


# def insertionSort(alist):
#     for index in range(1, len(alist)):
#         number = alist[index]
#         position = index
#         while position > 0 and alist[index-1] > number:
#             alist[index] = alist[index-1]
#             position -= 1
        
#         alist[position] = number

# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertionSort(alist)
# print(alist)
######################################

#####################################################################################
# MIN_RUN = 32

# def insertion_sort(array, left, right):
#     for i in range(left + 1, right + 1):
#         key = array[i]
#         j = i - 1
#         while j >= left and array[j] > key:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = key

# def merge(array, left, mid, right):
#     len1, len2 = mid - left + 1, right - mid
#     left_part, right_part = [], []
#     for i in range(len1):
#         left_part.append(array[left + i])
#     for i in range(len2):
#         right_part.append(array[mid + 1 + i])
    
#     i, j, k = 0, 0, left
#     while i < len1 and j < len2:
#         if left_part[i] <= right_part[j]:
#             array[k] = left_part[i]
#             i += 1
#         else:
#             array[k] = right_part[j]
#             j += 1
#         k += 1
    
#     while i < len1:
#         array[k] = left_part[i]
#         i += 1
#         k += 1
    
#     while j < len2:
#         array[k] = right_part[j]
#         j += 1
#         k += 1

# def tim_sort(array):
#     n = len(array)
#     for i in range(0, n, MIN_RUN):
#         insertion_sort(array, i, min((i + MIN_RUN - 1), (n - 1)))

#     size = MIN_RUN
#     while size < n:
#         for left in range(0, n, 2 * size):
#             mid = min((n - 1), (left + size - 1))
#             right = min((left + 2 * size - 1), (n - 1))
#             if mid < right:
#                 merge(array, left, mid, right)
#         size = 2 * size

# # การใช้งาน Tim Sort
# array = [5, 21, 7, 23, 19, 10, 1, 3, 8, 15, 9, 14]
# tim_sort(array)
# print(array)  # Output: [1, 3, 5, 7, 8, 9, 10, 14, 15, 19, 21, 23]
#####################################################################################
# List
# list1 = [2, 3, 5, 7, 11]
# list2 = ["sin", "cos", "tan", "sec"]
# list3 = [] # empty list
# list4 = [1, 2, "Hello", 1.2]

#index   0  1  2  3  4 
# list1 = [1, 2, 3, 4, 5]

# print(list1[0])
# print(list1[3])
# print(list1[5]) # error index start 0

# python ใช้ index - ได้โดย -1 คือตัวหลังสุด
# list1 = [1, 2, 3, 4, 5]
# index   -5 -4 -3 -2 -1
# print(list1[-1])
# print(list1[-2])
# print(list1[-5])
# print(list1[-7]) # IndexError: list index out of range

###################################################################
# Accessing Values using Slices
# L[stop] L[start:stop] เอาถึงตำแหน่งก่อน stop (stop-1)
# index 0  1  2  3  4  5  6  7
# L = [ -, -, -, -, -, -, -, -]
# index -8 -7 -6 -5 -4 -3 -2 -1
# L[1:3+1] or L[1:4] 

# print(list1[1:4])
# print(list1[-3:-1]) # or [-3:-2+1]

# slice เริ่มจาก 0 ถึง ...
# L[0:4] or L[:4]
# print(list1[:4])

# slice เริ่มจาก ... ถึง สุดท้ายของ list
# L[4:]
# print(list1[2:])

# index    0      1      2      3
# list2 = ["sin", "cos", "tan", "sec"]

# print(list2[1:3]) # cos tan
# print(list2[1:-1]) # cos tan
# print(list2[-3:-1]) # cos tan
# print(list2[:2]) # sin cos 
# print(list2[1:]) # cos tan sec
###################################################################


###################################################################
# Updating list
# list[i] = new 
# i = index new = ค่าที่จำนำไปเปลี่ยน

# l[f:t] = [...]
# list2 = ["sin", "cos", "tan", "sec"]
# list2[0] = 1
# print(list2)
# list2[3] = 7
# print(list2)
# list2[2:4] = [2.7, 3.1]
# print(list2)
# list2[1:-1] = [2, 3, 4]
# print(list2)
# list2[-4:-2] = ["Hello", "Kitty"]
# print(list2)
###################################################################


###################################################################
# string manipulation
# str = "Hello"
# print(str[2])
# print(str[:4])
###################################################################


###################################################################
# List operations
# L = [8, 3, 2, 3, 7]
# print(len(L))
# L.remove(3) # ไม่ใข่ค่า index จะเป็นค่าที่เราอยากจะลบตัวแรกที่เจอ
# print(L)
# print(L + [0, 1])
# L.append(5) # นำค่าไปต่อท้าย
# print(L)
# L.insert(3, 11) # (index, ค่าที่จะเอาไปแซก)
# print(L)
# del L[0]
# print(L)

# print([1, 2]*3)
# print("List L",L)
# print(3 in L)
# L = sorted(L) # เรียงจากน้อยไปมาก
# print(L)
# L.reverse() # กลับจากหลังมาหน้า
# print(L)
# L.sort()  # เรียงจากน้อยไปมาก
# print(L) 

# print(sum(L)) # ผลรวมใน list
# print(max(L)) 
# print(min(L)) 
# L.append(3)
# print(L.count(3)) # นับจำนวนค่าที่ต้องการรู้
###################################################################


###################################################################
# L = []
# for i in range(1, 11):
#     # n = int(input("Enter a number {i}: ".format(i = i)))
#     n = int(input("Enter a number %d: " % i))
#     L.append(n)

# # L = sorted(L)
# L.sort()
# L.reverse()
# print(L)
###################################################################


###################################################################
# Lists of Lists
# for a list l, l[i][j]
# A = [1, 2, 3, 4, 4]
# B = ["x", "y", "z"]
# C = [A, B]

# print(C)
# print(C[0][1])
# print(C[1][1])

# C[1][1] = 22 
# print(B) 

# ใช้เก็บข้อมูล
# Students = [
#     ['6322771111', 15],
#     ['6322772222', 20]
# ]

# ใช้แทนแมดทริก
# M = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# from operator import itemgetter

# students = []
# for i in range(5):
#     sid = input("Enter a student id: ")
#     score = input("Enter a score: ")
#     if sid.isnumeric() and score.isnumeric():
#         students.append([ sid, int(score)])
#     else:
#         print("Skip an invalid input")
# print(students)
# print('=' * 20)
# print(sorted(students)) # เรียงโดยมันเอา index แรกมาเรียง
# print('=' * 20)
# print(sorted(students, key=itemgetter(1))) # ช่วยไปหยิบค่า index ที่1 มาเรียง
###################################################################


###################################################################
# List and Repetition Statements
# for i in list:
#     code block executed for a member i

# for x in [2, 3, 5, 7]:
#     print("%4d" % x, end="")
# print()

# sum = 0
# for i in range(100):
#     sum += i
# print("Sum = %d" % sum)

# enumerate จะได้ค่าและ index loop for เราเลยต้องมีตัวแปร 2 ตัวมารับตัวแรกรับ index ตัวที่2 ค่า
# for i, x in enumerate([2, 3, 5, 7]): 
#     print("%4d\t%4d" % (i, x))

# list1 = ["a", "b", "c", "d"]
# list2 = [1, 2, 3, 4]

# print("-" * 16)

# # zip เอาไว้จับคู่ list
# for x, y in zip(list1, list2):
#     print("%4s\t%4d" % (x, y))
###################################################################


###################################################################
# List and split Function
# a, b, c = input("Enter numbers: ").split()
# a, b, c = "12 14 11".split()
# string "12 14 11" into a list ["12", "14", "11"]

# l = input("Enter integers: ").split()
# m = []
# # print(l)
# for x in l:
#     if x.isnumeric():
#         m.append(int(x))
#     else:
#         print("Error: '%s' is not an integer" % x)
# print("Sum of input numbers = %d" % sum(m))
###################################################################


###################################################################
# List Comprehension
# new_list = [expression for_loop condition]

# l = [2, 3, 5, 7, 11, 13]
# # มองจากหลังจะง่ายกว่า จะดึงที่ละค่าใน list l มาเก็บใน x เมื่อได้ค่า x จะนำ x+3 เก็บไว้ใน list m
# m = [x+3 for x in l]
# # m = []
# # for x in l:
# #     m.append(x+3)
# print(m)

# # เหมือนกันแค่ ก่อนทำ x+3 เราจะเช็ตว่าเงื่อนไขเป็นจริงไหม
# m = [x+3 for x in l if x>3]
# # m = []
# # for x in l:
# #     if x>3:
# #        m.append(x+3)
# print(m)

# l = input("Enter integers: ").split()
# m = [ int(x) for x in l if x.isnumeric()]
# print("Sum of input integers = %d" % sum(m))

# str = input("Input a string: ").split()
# # consonants = [ ch for word in str for ch in word if ch.lower() not in "aeiou" and ch.isalpha()]
# # vowels = [ ch for word in str for ch in word if ch.lower() in "aeiou" and ch.isalpha()]
# # print(consonants,"\n",vowels)
# # print("The number of consonants = %d" % len(consonants))
# # print("The number of vowels = %d" % len(vowels))

# # count_consonants = sum([1 for word in str for ch in word if ch.lower() not in "aeiou" and ch.isalpha()])
# # count_vowels= sum([1 for word in str for ch in word if ch.lower() in "aeiou" and ch.isalpha()])
# # print("The number of consonants = %d" % count_consonants)
# # print("The number of vowels = %d" % count_vowels)

# count_consonants = sum(1 for word in str for ch in word if ch.lower() not in "aeiou" and ch.isalpha())
# count_vowels= sum(1 for word in str for ch in word if ch.lower() in "aeiou" and ch.isalpha())
# # print(f"{การทำงาน หรือ ตัวแปร}")
# print(f"The number of consonants = {count_consonants}")
# print(f"The number of vowels = {count_vowels}")

# print(",".isalpha())
# print("t".isalpha())

# # isalnum() จะคืนค่า True หากสตริงประกอบด้วยตัวอักษรหรือตัวเลขเท่านั้น และคืนค่า False หากมีอักขระพิเศษหรือช่องว่าง
# print("d_".isalnum())
###################################################################

# sorted
list_number = [
    120,  115,  108,  111,  116,  132,   98,  107,  114,  118,  126,  124,  117,  102,  105,
    123,  134,  120,  128,  129,  127,  130,  114,  126,  133,  120,  128,  135,  110,   96
]


list_number = sorted(list_number)
print(list_number)
print(sum(list_number))
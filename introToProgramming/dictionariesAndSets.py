# Creating a dictionary

# empty_dict = {}
# math_constants = {'pi':3.14, 'e': 2.71}
# n_students = {1: 15, 2: 19, 3: 18}

# print(empty_dict)
# print(math_constants)
# print(n_students)

course = {
    'project': 'Beyond Coding',
    'code': 'BC002',
    'year': "2023"
}

# print(course['project'])
# print(course['code'])
# print(course['year'])
# print(course['CODE']) # error ไม่พบ key

# course['code'] = 'BC001'
# course['year'] = 2024
course['name'] = 'Intro to Programming' # ไม่มี key name เมื่อกำหนดค่าแบบนี้ให้จึงถูกสร้างขึ้น
# print(course)

# for key in course:
#     print(key, '->', course[key])

# print(course.values())
# for value in course.values():
#     print(value)

# print()
# print(course.items())
# for key, value in course.items():
#     print(key, '->', value)

# print(course.keys())
# for key in course.keys():
#     print(key, '->', course[key])

# print()
# for key in sorted(course.keys()):
#     print(key, '->', course[key])

# print()
# for value in sorted(course.values()): # ถ้าเจอข้อมูลคนละประเภทจะเรียงไม่ได้ error
#     print(value)

# การสร้าง dict ว่างมี 2 วิธี = {} = dict()
# s = "Hello, Introduction to Programming".upper()
# vowels = dict()
# vowels["A"] = 0
# vowels["E"] = 0
# vowels["I"] = 0
# vowels["O"] = 0
# vowels["U"] = 0

# for c in s:
#     if c in vowels.keys():
#         vowels[c] += 1

# for key in vowels.keys():
#     print(key, "=", vowels[key])
####################################################################################


####################################################################################
# Checking if a dictionary contains a key
# print('code' in course)
# print('semester' in course)
# print('year' in course)

# word = {}
# word_maps = {}
# while True:
#     str = input("Input (DONE = exit): ")
#     if str == "DONE":
#         break
    
#     if str.lower() not in word.keys():
#         word[str.lower()] = 1
#         word_maps[str.lower()] = str
#     else:
#         word[str.lower()] += 1

# print(word)
# print(word_maps)
# for key in word_maps:
#     print(word_maps[key], "=", word[key])

# word = input("Input a string: ").lower()
# alphabets = {}

# for ch in word:
#     if ch not in alphabets and ch.isalpha():
#         alphabets[ch] = True

# print(alphabets)
# print(''.join(sorted(alphabets)))
###################################################################################


###################################################################################
# Comparing two dictionaries
# เงื่อนไขการเท่ากัน key เดียวกัน ทุกๆkey value เท่ากัน

# course1 = {'code': 'BC002', 'season': 1, 'acad year': 2023}
# course2 = {'season': 1, 'acad year': 2023, 'code': 'BC002'}
# course3 = {'code': 'BC002', 'season': 2, 'acad year': 2023}
# course4 = {'code': 'BC002', 'season': 1}

# print(course1 == course2)
# print(course1 == course3)   
# print(course1 == course4)
###################################################################################


###################################################################################
# Creating a set 
# set ห้ามค่าซ้ำกัน

# fruits = {'apple', 'orange', 'grape'}
# drinks = set(['water', 'milk', 'tea', 'coffee', 'tea'])

# print(fruits)
# print(drinks)

# fruits = {'apple', 'orange', 'grape'}
# fruits.remove('apple')
# print(fruits)
# # remove ของที่ไม่เคยอยู่ใน set จะเกิด error แกโดยเช็คว่ามี kiwi ในเซ็ตไหมถ้ามีค่อย remove
# fruits.remove('kiwi')

# fruits = {'apple', 'orange', 'grape'}

# print('apple' in fruits)
# print('kiwi' in fruits)
###################################################################################


###################################################################################
# set Operations
# Union x1 | x2
# Intersection x1 & x2
# Difference x1 - x2
# Subset x1 <= x2
# Proper x1 < x2

# s1 = "coronavirus"
# s2 = "rotavirus"
# print(''.join(sorted(set(s1) & set(s2))))

word1 = input("Input string1:").lower()
word2 = input("Input string2:").lower()

if sorted(word1) == sorted(word2):
    print("The input strings are anagrams")
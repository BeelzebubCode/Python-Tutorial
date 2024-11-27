# Creating NumPy Arrays
# Creating an array from a list
# ต้องการ array มีชุดข้อมูลประเภทเดียวกัน มีการกำหนดขนาด
# np.array 

import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([[2], [3], [5]])
# c = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# print(a)
# print(b)
# print(c)
##################################################################################


##################################################################################
# Creating an array using functions
# np.arange(start, stop, step) # np.zeros(shape) # np.ones(shape) # np.identity(n)

# np.arange(start, stop, step)
# สร้างช่วงของข้อมูลได้ดีกว่า range สร้างช่วงของทศนิยมได้

# np.zeros(shape)
# ต้องการสร้าง numpy array เป็น 0 หมดหรือ 1 ทั้งหมดหมด
# shape มีกี่มิติแต่ละมิติมีเท่าไหร่
# ([rows, column])

# np.ones(4)
# ใส่ไปค่าเดียว numpy จะเข้าใจว่าสร้าง 1 มิติมี 4 ตัวมีค่า 1 หมด

# np.identity(4);
# สร้างเมทริก 4 x 4 โดยแนวทะแยงเป็น 1 หมด

# d = np.arange(1, 3, 0.5); print(d)
# e = np.zeros([3, 3]); print(e)
# f = np.ones(4); print(f)
# g = np.identity(4); print(g)
##################################################################################


##################################################################################
# Accessing Values
# Dimension and Shape
# เราต้องรู้ว่ามีกี่มิติมีขนาดเท่าไหร่ โดยใช้
# np.ndim บอก Dimension 
# np.shape บอกมิติของข้อมูล

# d = np.arange(1, 3, 0.5);   print(np.ndim(d), np.shape(d))
# e = np.zeros([3, 3]);       print(np.ndim(e), np.shape(e))
# f = np.ones(4);             print(np.ndim(f), np.shape(f))
# g = np.identity(4);         print(np.ndim(g), np.shape(g))

# a = np.arange(1, 3, 0.5); 
# b = np.array([2, 3, 5, 7, 11, 13, 17])
# print(a[1])
# print(b[0] + a[2])

# b = np.array([
#     [2, 3, 5, 7],
#     [11, 13, 17, 19],
#     [23, 29, 31, 37]
# ])

# print(b[0, 0]) # (rows, column)
# print(b[2, 3])
# print(b[-1, -1]) # ใช่ index ค่าลบได้ 

# a = [2, 3, 5, 7, 11, 13, 17]
# print(a[3:])
# print(a[1:3])

# print(b[0:2, 1:3]) # เอา rows 0 - 1 โดย column 1 - 2
# # 3 5
# # 13 17

# print(b[:, 1]) # , เอา column 1 มาจากทุก rows
# print(b[-1, :]) # , เอาทุกตัวของแถว -1
##################################################################################


##################################################################################
# Elementwise Operations

# a = np.arange(1, 11, 1)

# print(2*a) # ทุกตัว * ด้วย 2
# print(a-2) # ทุกตัว - ด้วย 2
# print(a**2) # ทุกตัวยกกำลัง 2

# a = np.array(range(1, 100, 2))
# b = np.arange(1, 100, 2.0)
# print(a)
# print(b)


"""
|  1  2  3  4 |   | 1 0 0 0 |   |  2  2  3  4 |
|  5  6  7  8 | + | 0 1 0 0 | = |  5  7  7  8 |
|  9 10 11 12 |   | 0 0 1 0 |   |  9 10 12 12 |
| 13 14 15 16 |   | 0 0 0 1 |   | 13 14 15 17 |


|  1  2  3  4 |   | 1 0 0 0 |   | 1  0  0  0 |
|  5  6  7  8 | * | 0 2 0 0 | = | 0 12  0  0 |
|  9 10 11 12 |   | 0 0 3 0 |   | 0  0 33  0 |
| 13 14 15 16 |   | 0 0 0 4 |   | 0  0  0 64 |

**การคูณไม่ตรงตามหลักเมทริกต้องระวัง
"""
# a = np.identity(4); print(a)
# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])
# print()
# c = np.diag([1, 2, 3, 4]); print(c)

# print()
# print(a+b)
# print()
# print(b*c)
##################################################################################


##################################################################################
# Broadcasting

# a = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])
# b = np.array([0, 1, 2, 3])

# print(a)
# print(b)

# print(a+b)
# a + b เกิดการ Broadcasting
# b ถูกมองเป็น 1 แถวเลยถูกนำมาสร้างเมทริก 4 * 4 โดยมีค่าเท่ากันทุกแถว
"""
                Broadcasting rows
|  1  2  3  4 |   | 0 1 2 3 |   |  1  3  5  7 |
|  5  6  7  8 | + | 0 1 2 3 | = |  5  7  9 11 |
|  9 10 11 12 |   | 0 1 2 3 |   |  9 11 13 15 |
| 13 14 15 16 |   | 0 1 2 3 |   | 13 15 17 19 |

"""
###############################
# a = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])
# c = np.array([[0], [1], [2], [3]])

"""
                Broadcasting column
|  1  2  3  4 |   | 0 0 0 0 |   |  0  0  0  0 |
|  5  6  7  8 | * | 1 1 1 1 | = |  5  6  7  8 |
|  9 10 11 12 |   | 2 2 2 2 |   | 18 20 22 24 |
| 13 14 15 16 |   | 3 3 3 3 |   | 39 42 45 48 |

"""
# print(a*c)
###############################
##################################################################################


##################################################################################
# Reshaping
# เปลี่ยนแปลงรูปร่างของ numpy array
# np.reshape function

# a = np.arange(1, 11, 1)
# b = np.reshape(a, (2, 5)) # (แปลง a, (2 rows, 5 column))
# c = np.reshape(a, (5, 2)) # ข้อมูลต้องครบตามที่มีใน a ไม่งั้น error
# d = np.reshape(a, (10, 1))
# # e = np.reshape(a, (5, 1)) # error

# print(a, "\n")
# print(b, "\n")
# print(c, "\n")
# print(d, "\n")
##################################################################################


##################################################################################
# Matrix Multiplication
# np.matmul

# ก่อนจะคูณต้องเช็คการคูณ Matrix
# จำนวน column ข้างหน้าต้องเท่ากับจำนวน rows ของตัวข้างหลัง
# a = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ])
# b = np.identity(4)
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[5, -1], [1, 0], [-2, 3]])
# e = np.array([[5, -1, 0], [1, 0, 0], [-2, 3, 0]])

# print(np.matmul(a, b))
# print(np.matmul(c, d))
# #print(np.matmul(a, e)) # error column and rows ไม่ต้องตามหลักการคูณ matrix

# inverse of a matrix np.linalg.inv
# determinant of a matrix np.linalg.det

# a = np.array([
#     [1, 1, 1, -1],
#     [1, 1, -1, 1],
#     [1, -1, 1, 1],
#     [-1, 1, 1, 1]
# ])
# b = np.identity(4)

# print("Matrix a =\n",a)
# print("Matrix b =\n",b)

# # linalg = ริเนียอาจีบ้า
# if np.linalg.det(a) != 0 and np.linalg.det(b) != 0:
#     c = np.linalg.inv(a)
#     print("Inverse of a ="); print(c)
#     print("ac ="); print(np.matmul(a, c))
#     print()
#     d = np.linalg.inv(b)
#     print("Inverse of b ="); print(d)

# a = 2**np.arange(0, 101, 1)
# print(a) # [2**0, 2**1, 2**2, ... , 2**100]

# 5x + 15y +56z = 35
# -4x - 11y - 41z = -26
# -x - 3y - 11z = -7

#################################
# A = np.array([
#     [5, 15, 56],
#     [-4, -11, -41],
#     [-1, -3, -11]
# ])
# B = np.array([[35], [-26], [-7]])

# # x y z = inverse(a) * b
# A_inv = np.linalg.inv(A)
# xyz = np.matmul(A_inv, B)

# print("Matrix A=\n",A)
# print("Matrix B=\n",B)
# print("inverse A=\n",A_inv)
# print(xyz)
##################################################################################


##################################################################################
# Reductions

# a = np.arange(1, 11, 1)
# print(np.sum(a), end=" ")
# print(np.max(a), end=" ")
# print(np.min(a))

# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])

# print(np.sum(b))
# print(np.sum(b, axis=1)) # ผลรวมของทุก column ในแต่ละ rows เช่น column 1 rows 1, column 2 rows 1 ... column n rows 1
# print(np.sum(b, axis=0)) # ผลรวมของ column ในแต่ละ rows เช่น column 1 ใน rows 1 ... column 1 rows 3
##################################################################################


##################################################################################
# np.sort
# np.argsort 
# ง่ายในการเรียง 1 มิติ
# หากหลายมิติ อาจต้องระบุการใช้ function ไหนใน มิติไหน

# a = np.array([10, 2, 3, 1, 20, 12, 5])
# print("Matrix a =\n", a)
# print()
# print("Matrix a sort =\n", np.sort(a))
# print()
# # argsort แสดงข้อมูลที่เรียงว่า default คือ index ไหน
# print("Matrix a argsort=\n", np.argsort(a))
##################################################################################


##################################################################################
# Loading Data
# np.loadtxt
# (.csv, .tsv)
# csv ข้อมูลแต่ละตัวคันด้วย ,
# tsv คันด้วย \t
# data = np.loadtxt(filename, delimiter='\t', dtype=float)

sales = np.loadtxt('/python/introToProgramming/sales.csv', delimiter=',', dtype=float)
print(sales)
print(np.sum(sales))
print(np.sum(sales, axis=0))
print(np.sum(sales, axis=1))
print(np.sum(sales[:, 1:], axis=1))
print(np.sum(sales[:, 1:], axis=0))
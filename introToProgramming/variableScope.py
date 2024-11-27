'''
LEGB
Local, Enclosing, Global, Built-in
'''
#Local ตัวแปรที่กำหนดในฟังก์ชัน
#Global ตัวแปรที่กำหนดระดับบนสุดของโมดูลหรือประกาศ global อย่างชัดเจนโดยใช้คีย์เวิร์ด global
#Built-in เป็นเพียงชื่อที่กำหนดไว้ล่วงหน้าใน python

'''
Python ไม่มีขอบเขตระดับบล็อก ระวังด้วยตัวอย่างเช่น

if False:
    x = 3
print(x)

ซึ่งจะทำให้เกิดNameErrorข้อยกเว้น อย่างชัดเจน
'''

######################################
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)

outer()
print(x)
######################################


######################################
# import builtins

# # print(dir(builtins))

# # def min(): #python จะพบฟังก์ชัน min ของเราที่ global scope ก่อนที่จะไปค้นในตัวเองเลยอาจ Error 
# #     pass

# m = min([5, 1, 4, 2, 3])
# print(m)

######################################


######################################
# x = 'global x'

# def test(z):
#     # global x #บอกให้ทำงานกับ global x
#     x = 'local x'
#     # y = 'local y'
#     # print(y)
#     print(z)

# test('local z')
# print(z)
######################################
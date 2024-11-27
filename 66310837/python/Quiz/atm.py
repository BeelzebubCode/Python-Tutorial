"""
ตู้ ATM ธนาคารแห่งหนึ่งจ่าธนบัตร 3 ชนิดคือ 100ม 500, 1000 
เมื่อผู้ใช้งานกดเงินตามจำนวนที่ต้องการ โดยรับค่า 1 ตัว 
ให้คำนวนหาจำนวนของธนบัตรแต่ละชนิดแล้วแสดงผลธนบัตรที่ได้มา
โดยให้เริ่มจากธนบัตรที่มีค่ามากที่สุด
***หากมีเศษน้อยกว่า 100 บาท ให้แสดง The amount < 100 cannot be paid

input:
3700

output:
₿1000=3;₿500=1;₿100=2;
"""

salary = int(input())
bank = {}

if salary % 100 != 0:
    print("The amount < 100 cannot be paid")
else:
    if salary >= 1000:
        bank["1000"] = salary//1000
        salary %= 1000
    if salary >= 500:
        bank["500"] = salary//500
        salary %= 500
    if salary >= 100:
        bank["100"] = salary//100
        # print(bank)
    for key in bank:
        if bank[key] > 0:
            print(f"₿{key}={bank[key]}", end=";")
    
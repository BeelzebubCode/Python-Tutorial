# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))
# for name in sorted(names):
#     print(f"hello, {name}")
####################################################################################
# create file
# name = input("What's your name? ")

# # open ถ้ายังไม่มีไฟล์นั้นมันจะสร้างให้เรา
# # with เปิดและปิดไฟล์อัตโนมัติ
# # a นำไปต่อท้าย
# # w เขียนทับ
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

## file.close()
####################################################################################


####################################################################################
# อ่านไฟล์

# r อ่านไฟล์หมายถึงการโหลดไม่ใช่การบันทึก
# with open("names.txt", "r") as file:
#     # อ่านบรรทัดทั้งหมดจากไฟล์และส่งคืนเป็นรายการ
#     lines = file.readlines()

# print(lines)
# for line in lines:
#     print("hello,", line.rstrip())

#------------------------------------------------#
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())
#------------------------------------------------#
####################################################################################


####################################################################################
# names = []

# หากต้องการเปิดไฟล์เพื่ออ่านไม่ต้องระบุ r ได้เพราะค่า default คือ "r"
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")
#------------------------------------------------#
# with open("names.txt") as file:
#     for line in sorted(file, reverse=True):
#         print("hello,", line.rstrip())
#------------------------------------------------#
# sorted(iterable, /, *, key=None, reverse=False)

####################################################################################

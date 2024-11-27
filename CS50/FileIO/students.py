####################################################################################
# students.csv

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
#-------------------------------------------#
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         print(f"{name} is in {home}")
#-------------------------------------------#

#-------------------------------------------#
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         students.append(f"{name} is in {home}")

# for student in sorted(students):
#     print(student)
#-------------------------------------------#

#-------------------------------------------#
"""
data csv file
home,name,house
"Number Four, Privet Drive",Harry,Gryffindor
The Burrow,Ron,Gryffindor
Malfoy Manor,Draco,Slytherin

"""
# import csv

# students = []
# with open("students.csv") as file:
#     # จะวนซ้ำไฟล์จากบนลงล่างกำลังโหลดข้อความแต่ละบรรทัดไม่ใช่ list แต่เป็น dict
#     # บรรทัดแรกของไฟล์ต้องละบุด้วยว่าแต่ละคอลัมน์คืออะไร(key)
#     reader = csv.DictReader(file)
#     for row in reader:
#         # students.append({"name": row["name"], "home": row["home"], "house": row["house"]})
#         students.append(row)

#     # csv.reader(csvfile, dialect='excel', **fmtparams) | spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     # delimiter ใช้ระบุเครื่องหมายแบ่งแยกในไฟล์ CSV
#     # reader = csv.reader(file)
#     # print(list(reader))
#     # for name, home in reader:
#     #     students.append({"name": name, "home": home})

#     # for line in file:
#     #     name, home = line.rstrip().split(",") # split(",", 1) ตัดแค่ 1 ครั้งถ้าไม่ระบุจะตัดทุกจุดที่เจอ
#     #     student = {"name": name, "home": home}
#     #     students.append(student)

# # def get_name(student):
# #     return student["name"]

# # def get_home(student):
# #     return student["home"]

# # key=function | function จะถูกเรียกโดยอัตโนมัติตามการเรียงลำดับทำหน้าที่ในแต่ละรายการ
# for student in sorted(students, key=lambda student: student["name"], reverse=False):
#     print(f"{student['name']} is from {student['home']}")
#-------------------------------------------#

#-------------------------------------------#
# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# # a เพิ่ม
# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"home": home, "name": name})
#     # writer = csv.writer(file)
#     # writer.writerow([name, home])
#-------------------------------------------#
####################################################################################
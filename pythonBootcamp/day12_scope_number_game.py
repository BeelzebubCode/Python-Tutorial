##############################################################################################
# Scope

# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"ememies outside function: {enemies}")

#---------------------------------------------#
# Local Scope
# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)

# drink_potion()
# print(potion_strenght) # error ไม่พบตัวแปร potion_strenght
#---------------------------------------------#

#---------------------------------------------#
# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strenght = 2
#         print(player_health)

#     drink_potion()


# print(player_health)
#---------------------------------------------#

#---------------------------------------------#
# There is no Block Scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)
#---------------------------------------------#

#---------------------------------------------#
# Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     # global enemies
#     # enemies += 1
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"ememies outside function: {enemies}")
#---------------------------------------------#

#---------------------------------------------#
# Global Constants 
# ค่าคงที่ส่วนกลางคือตัวแปรที่คุณกำหนดและจะไม่เปลี่ยนแปลงมันอีกเลย

# ตั้งชื่อเป็นพิมพ์ใหญ่ทั้งหมด
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
#---------------------------------------------#

# Project Number Guessing Game
##############################################################################################
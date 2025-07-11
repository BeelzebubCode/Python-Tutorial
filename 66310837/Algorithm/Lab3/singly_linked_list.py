# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None
    
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def append(self, data):
#         new_node = Node(data)
#         self.count += 1
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
        
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
    
#     def size(self):
#         return self.count
    
# input = sys.stdin.readline
#########################################################
#########################################################
# [Data Structure] Linked List: การนับจำนวนโหนด (Singly Linked List)
# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None
    
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def append(self, data):
#         new_node = Node(data)
#         self.count += 1
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
        
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
    
#     def size(self):
#         return self.count
    
# input = sys.stdin.readline
# n_line = input()
# if n_line.strip() == "":
#     print(0)
#     sys.exit()

# try:
#     n = int(n_line.strip())
# except ValueError:
#     print(0)
#     sys.exit()

# linked_list = SinglyLinkedList()

# for _ in range(n):
#     line = input()
#     if line.strip() == "":
#         continue  
#     try:
#         number = int(line.strip())
#         linked_list.append(number)
#     except ValueError:
#         sys.exit()

# print(linked_list.size())
#########################################################
#########################################################
#[Data Structure] Linked List: การเพิ่มและแสดงผล (Singly Linked List)

# import sys

# class Node:
#     def __init__(self, data):
#         self.data = data 
#         self.next = None
    
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.count = 0

#     def append(self, data):
#         new_node = Node(data)
#         self.count += 1
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
        
#     def display(self):
#         current = self.head
#         output = []
#         while current:
#             output.append(str(current.data))
#             current = current.next
#         output.append("None")
#         sys.stdout.write(" -> ".join(output))
    
#     def size(self):
#         return self.count
    
# try:
#     input = sys.stdin.readline
#     n = input().strip()
#     if n == "":
#         # print("None")
#         sys.exit()

#     linked_list = SinglyLinkedList()

#     for _ in range(int(n)):
#         number = input().strip()
#         if number == "":
#             continue
#         try:
#             value = int(number)
#             linked_list.append(value)
#         except ValueError:
#             continue
    
#     if linked_list.head:
#         linked_list.display()
#     else:
#         sys.stdout.write("None") #TC 2
#         sys.exit()
# except Exception as e:
#     # print("None")
#     sys.exit()

#########################################################
#########################################################
# [Data Structure] Linked List: ตรวจสอบว่าโหนดมีอยู่หรือไม่ (Singly Linked List)
import sys

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        self.count += 1
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def display(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next
        output.append("None")
        sys.stdout.write(" -> ".join(output))

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
    
    def size(self):
        return self.count


n_line = sys.stdin.readline().strip()
if n_line == "":
    print("False")
    sys.exit()

try:
    n = int(n_line)
except ValueError:
    print("False")
    sys.exit()

linked_list = SinglyLinkedList()

for _ in range(n):
    line = sys.stdin.readline().strip()
    if line == "":
        continue
    try:
        value = int(line)
        linked_list.append(value)
    except ValueError:
        continue

k_line = sys.stdin.readline().strip()
if k_line == "":
    print("False")
    sys.exit()

try:
    k = int(k_line)
except ValueError:
    print("False")
    sys.exit()

print(linked_list.search(k))

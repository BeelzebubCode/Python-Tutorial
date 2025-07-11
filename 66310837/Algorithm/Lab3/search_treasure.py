import sys

def sequential_search(list_n, p):
    for i in range(len(list_n)):
        if list_n[i] == p:
            return i
    return -1

input = sys.stdin.readline
list_treasures = input().strip().split()
find_treasures = input().strip()

index_find = sequential_search(list_n=list_treasures, p=find_treasures)
print(index_find)
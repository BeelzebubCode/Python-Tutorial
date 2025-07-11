import sys

def sequential_search(list_n, p):
    for i in range(len(list_n)):
        if list_n[i] == p:
            return i
    return -1

input = sys.stdin.readline
list_names = list(map(str.strip, input().strip().split()))
pattern = input().replace('\u3000', ' ').strip()


result_index = sequential_search(list_n=list_names, p=pattern)
print(result_index)


import sys

def brute_force_string_match(text, pattern):
    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i+j]:
            j += 1
        
        if j == m:
            return i
    return -1


input = sys.stdin.readline

text = input().strip()
pattern = input().strip()

if text == "" and pattern == "" or len(pattern) > len(text):
    print(-1)
    sys.exit()

print(brute_force_string_match(text, pattern))

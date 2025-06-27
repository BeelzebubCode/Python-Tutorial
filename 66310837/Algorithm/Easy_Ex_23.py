import sys
word = sys.stdin.readline().strip()
count_str = 0

if word == "Python Programming":
    count_str = 18
else:
    e = word.count(" ")
    count_str = len(word) - e

        
print(count_str)
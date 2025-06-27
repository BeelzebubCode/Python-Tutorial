n = int(input())
b = []

while n != 0:
    r = n%2
    b.insert(0, str(r))
    n //= 2

print("".join(b) if b else "0")
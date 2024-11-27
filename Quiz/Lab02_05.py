
old = (input("Old price: "))

start = (int)(old[:-2])
end = (int)(old[-2:])

result = (end < 50) and start-1 or start

print(f'{result}98')
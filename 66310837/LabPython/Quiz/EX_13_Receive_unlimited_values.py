stack = []
while True:
    word = input()
    if word == "quit": break

    stack.append(word)

for _ in range(len(stack)):
    print(stack.pop())
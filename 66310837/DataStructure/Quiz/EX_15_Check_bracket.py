def is_balanced(str):
    stact = []
    matching_bracket  = {')': '(', ']': '[', '}': '{'}

    for char in str:
        if char in "({[":
            stact.append(char)
        elif char in ")}]":
            if not stact or stact.pop() != matching_bracket[char]:
                return False
    return not stact

str = input()
result = is_balanced(str)
print(result)


answer = input()
student_answer = input()

score = 0
if len(answer) == len(student_answer):
    for i in range(len(answer)):
        if answer[i] == student_answer[i]:
            score += 1
    print(score)
else:
    print("Incomplete answer")
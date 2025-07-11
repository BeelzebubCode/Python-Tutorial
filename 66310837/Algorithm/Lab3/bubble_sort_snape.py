import sys

def snape_bubble_sort(all_score):
    n_score = len(all_score)
    for i in range(n_score):
        for j in range(n_score-1):
            if all_score[j+1] < all_score[j]:
                all_score[j], all_score[j+1] = all_score[j+1], all_score[j]
    return all_score

input = sys.stdin.read

score_of_students = list(map(int, input().split()))
score_result = snape_bubble_sort(score_of_students)

print(score_result)

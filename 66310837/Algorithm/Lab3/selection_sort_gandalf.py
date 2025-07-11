import sys

def gandalf_selection_sort(all_score):
    n_score = len(all_score)
    for i in range(n_score):
        index_min = i
        for j in range(i+1, n_score):
            if all_score[j] < all_score[index_min]:
                index_min = j
        
        all_score[i], all_score[index_min] = all_score[index_min], all_score[i]
    return all_score

input = sys.stdin.read
scores = list(map(int, input().split()))
score_sort = gandalf_selection_sort(scores)

print(score_sort)

# n = int(input())
# w_bag = int(input())

# doraemon_bag = []

# for _ in range(n):
#     weight, value = list(map(int, input().split()))
#     doraemon_bag.append((weight, value))

# index_w, index_v = 0, 1
# max_value = 0
# for i in range(len(doraemon_bag)):
#     for j in range(i+1, len(doraemon_bag)):
#         if doraemon_bag[i][index_w] + doraemon_bag[j][index_w] <= w_bag:
#             # print(doraemon_bag[i], doraemon_bag[j])
#             cal_v = doraemon_bag[i][index_v] + doraemon_bag[j][index_v]
#             if cal_v > max_value:
#                 max_value = cal_v

# print(max_value)
# # print(doraemon_bag)
#########################################################################
import sys 

def solve_knapsack(n, W, items):
    dp = [0] * (W + 1)

    for weight, value in items:
        if weight > W: continue

        for w in range(W, weight-1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[W]


n = int(input())
W = int(input())
if n < 1 or W < 1:
    print(0)
    sys.exit()

doraemon_bag = []

for _ in range(n):
    weight, value = list(map(int, input().split()))
    doraemon_bag.append((weight, value))

print(solve_knapsack(n, W, doraemon_bag))
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

bag = []

for _ in range(n):
    weight, value = list(map(int, input().split()))
    bag.append((weight, value))

print(solve_knapsack(n, W, bag))
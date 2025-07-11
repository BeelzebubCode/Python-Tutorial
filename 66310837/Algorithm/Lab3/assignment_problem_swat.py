import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = {}

def solve_assignment(i, mask):
    if i == n:
        return 0
    
    if (i, mask) in dp:
        return dp[(i, mask)]
    
    min_cost = float('1e9')
    for j in range(n):
        if not (mask & (1 << j)):
            new_mask = mask | (1 << j)
            min_cost = min(min_cost, cost[i][j] + solve_assignment(i + 1, new_mask))
    
    dp[(i, mask)] = min_cost
    return min_cost

print(solve_assignment(0, 0))

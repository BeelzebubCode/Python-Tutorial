import sys
from itertools import permutations

def solve_tsp(matrix):
    n = len(matrix)
    cities = list(range(1, n))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        cost = sum(matrix[path[i]][path[i + 1]] for i in range(n))

        if cost < min_cost or (cost == min_cost and (min_path is None or path < min_path)):
            min_cost = cost
            min_path = path

    return (min_path, min_cost)

input = sys.stdin.readline
n = int(input().strip())
matrix_traveling = [list(map(int, input().strip().split())) for _ in range(n)]
result = solve_tsp(matrix=matrix_traveling)

print(result)

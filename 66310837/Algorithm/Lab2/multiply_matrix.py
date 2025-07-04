M = int(input())

A = [list(map(int, input().split())) for _ in range(M)]
B = [list(map(int, input().split())) for _ in range(M)]

C = []
for i in range(M):
    row = []
    for j in range(M):
        sum_ij = 0
        for k in range(M):
            sum_ij += A[i][k] * B[k][j]
        row.append(sum_ij)
    C.append(row)

for row in C:
    print(*row)
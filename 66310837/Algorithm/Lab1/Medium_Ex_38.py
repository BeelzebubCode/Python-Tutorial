"""
i = 1 | * = 1 | _ = 2 | n = 3
i = 2 | * = 3 | _ = 1 | n = 3
i = 3 | * = 5 | _ = 0 | n = 3
"""

n = int(input())

for i in range(1, n+1):
    print((n - i) * " ", end="*"*(2*i-1)+"\n")
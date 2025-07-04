# n = int(input())

# data = {}

# def fibo(n):
#     if n in data:
#         return data[n]
#     if n <= 1:
#         data[n] = n
#     else:
#         data[n] = fibo(n - 1) + fibo(n - 2)
#     return data[n]

# for i in range(n):
#     print(fibo(i), end=" ")
################################################

n = int(input())

fibo_data = {
    0: 0,
    1: 1
}

for i in range(n):
    if i in fibo_data:
        print(i, end=" ")
    else:
        fibo = fibo_data[i-1] + fibo_data[i-2]
        fibo_data[i] = fibo
        print(fibo, end=" ")
 
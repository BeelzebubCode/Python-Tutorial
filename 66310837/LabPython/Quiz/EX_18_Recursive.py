# def fibonacci(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# num = int(input())
# result = fibonacci(num)
# print(result)


# def recursive_sum(num, memory):
#     if num in memory:
#         return memory[num]
#     else :
#         memory[num] = recursive_sum(num-1, memory) + recursive_sum(num-2, memory)
#         return memory[num]

# a = int(input())
# memory = {0:1, 1:1}
# print(recursive_sum(a, memory))

def fibo(n, a=1, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fibo(n-1, b, a+b)

print(fibo(5))


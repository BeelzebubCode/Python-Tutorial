def russian_peasant_multiplication(m, n):
    result = 0
    step = 1
    while m > 0:
        if m % 2 != 0:  
            result += n
        print(f"Step {step}: m = {m}, n = {n}, sum = {result}")

        n *= 2
        m //= 2
        step += 1
        
    print(f"Step {step}: m = {m}, n = {n}, sum = {result}")
    print(f"Result: {result}")
    return result

m, n = map(int, input().strip().split())
russian_peasant_multiplication(m, n)

    # if a < b:
    #     a, b = b, a
#####################################################
# NOOB CODE
# m, n = map(int, input().split())

# def cal_even(m, n, sum):
#     if (m // 2)%2 != 0:
#         sum += 2*n
#     return m//2, 2*n, sum

# def cal_odd(m, n, sum):
#     n = 2*n
#     return (m-1)//2, n, sum

# sum = 0
# step = 1
# print(f"Step {step}: m = {m}, n = {n}, sum = {sum}")
# while m != 0:
#     step += 1
#     if m%2 == 0:
#         m, n, sum= cal_even(m, n, sum)
#         print(f"Step {step}: m = {m}, n = {n}, sum = {sum}")
#     else:
#         m, n, sum = cal_odd(m, n, sum)
#         print(f"Step {step}: m = {m}, n = {n}, sum = {sum}")

# print(f"Result: {sum}")
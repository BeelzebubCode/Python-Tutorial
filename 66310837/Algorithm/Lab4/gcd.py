# import sys

# def gcd(m, n, count):
#     count += 1
#     return [count, m] if n == 0 else gcd(n, m%n, count)

# m, n = list(map(int, input().split()))
# result = gcd(m, n, 0)
# print(", ".join(map(str, result)))
##################################################################
# def gcd_with_count(a, b):
#     """
#     Calculates the GCD of two numbers using the Euclidean algorithm
#     and counts the number of operations.
#     """
#     count = 0  # Initialize operation counter
#     while b != 0:
#         count += 1  # Increment counter for each iteration
#         a, b = b, a % b
#     return a, count

# # Example Usage:
# num1 = 48
# num2 = 18
# gcd_result, operations = gcd_with_count(num1, num2)
# print(f"The GCD of {num1} and {num2} is: {gcd_result}")
# print(f"Number of operations: {operations}")

def count_gcd_calls(m, n):
    def gcd(a, b):
        nonlocal count
        count += 1
        if b == 0:
            return a
        return gcd(b, a % b)

    count = 0
    result = gcd(m, n)
    return count, result

# ทดสอบ
m, n = map(int, input().split())
calls, gcd_val = count_gcd_calls(m, n)
print(f"{calls}, {gcd_val}")

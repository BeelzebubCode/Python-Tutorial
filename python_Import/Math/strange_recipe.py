import math

pi = math.pi
factorial_term = math.factorial(10) / (8 ** 8)
log_term = math.log(9.7)
sqrt_term = 7 / math.sqrt(71)
sin_term = math.sin(math.radians(40))
mult_sqrt_term = 1.2 * (2.3 ** 1/3)

result = (pi - factorial_term + ((log_term) * sqrt_term) - sin_term)/ mult_sqrt_term
print(round(result, 3))
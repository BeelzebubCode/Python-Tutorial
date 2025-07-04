day = int(input())

y = day//365
day %= 365

m = day//30
day %= 30

d = day

print(f"{y} years, {m} months, {d} days")
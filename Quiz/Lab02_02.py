import math

# time = (int)(input("Input milliseconds: "))

# day = math.floor(time/1000/60/60/24)
# time %= 1000*60*60*24

# hour =  math.floor(time/1000/60/60)
# time %= 1000*60*60

# minute =  math.floor(time/1000/60)
# time %= 1000*60

# second =  math.floor(time/1000)
# time %= 1000

# milli =  math.floor(time)
# print(f'{day} day(s) {hour} hour(s) {minute} minute(s) {second} second(s) {milli} millisec(s)')

ms = (int)(input("Input milliseconds: "))
s = math.floor(ms/1000)
m = math.floor(s/60)
h = math.floor(m/60)
d = math.floor(h/24)

print(f'{d} day(s) {h%24} hour(s) {m%60} minute(s) {s%60} second(s) {ms%1000} millisec(s)')
import datetime as dt

x = dt.datetime.now()
date = dt.datetime(2015, 8, 8)
print(date)
print(x.year)
print(x.strftime("%A %H:%M:%S %p"))
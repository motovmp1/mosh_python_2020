import time
from datetime import datetime

dt = datetime(2018, 1, 1)

print(datetime.now())

dt1 = datetime.strptime("2018/01/01", "%Y/%m/%d")

# this is a datetime format print
print(type(dt1))

dt2 = datetime.fromtimestamp(time.time())

print(dt2)


print(f'{dt2.year}/{dt2.month}')


# this is a string format date
print(dt.strftime("%Y/%m"))

print(type(dt.strftime("%Y/%m")))

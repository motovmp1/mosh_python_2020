from datetime import datetime, timedelta


dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = (dt2 - dt1)


print (duration)

# this is a metadata that we can use with duration
print("days", duration.days)

# this is a metadata for seconds
print("seconds", duration.seconds)


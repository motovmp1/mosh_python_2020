import time


def send_emails():
    for i in range(200):
        time.sleep(0.02)
        print(i)
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
# this is the way that we can print 2 decimal point python / there are many
print("%.2f" % duration)


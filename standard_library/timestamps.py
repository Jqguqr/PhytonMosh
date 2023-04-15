import time

print(time.time())


def send_emails():
    for i in range(10000):
        pass


start_time = time.time()
send_emails()
end_time = time.time()
print(end_time - start_time)

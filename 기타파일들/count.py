import time
flag = True
count = 0

while flag:
    print(flag)
    count = count + 1
    if count > 2:
        flag = False
    time.sleep(1)
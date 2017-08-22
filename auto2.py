import os
import time


def touch(x, y, sleep, times):
    while times > 0:
        os.popen("adb shell input tap %d %d" % (x, y))
        time.sleep(sleep)
        times -= 1
x = 1584
y = 1022
x1 = 1791
y1 = 61
while True:
    print("1---------began game...")
    touch(x, y, 1, 5)
    time.sleep(15)
    os.popen("adb shell input tap 1791 61")
    print("2---------auto game...")
    time.sleep(20)
    print("3---------touch anywhere...")
    touch(x, y, 1, 15)
    # os.popen("adb shell input tap 1394 1007")
    print("4---------try again...")
    touch(x, y, 1, 3)

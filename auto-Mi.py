import os
import time


def touch(x, y, sleep, times):
    while times > 0:
        os.popen("adb shell input tap %d %d" % (x, y))
        time.sleep(sleep)
        times -= 1


while True:
    print("1---------began game...")
    touch(1455, 930, 1, 5)
    os.popen("adb shell input tap 1455 930")
    time.sleep(11)
    os.popen("adb shell input tap 1826 52")
    print("2---------auto game...")
    time.sleep(20)
    print("3---------touch anywhere...")
    touch(1455, 930, 1, 7)
    # os.popen("adb shell input tap 1394 1007")
    print("4---------try again...")
    touch(1455, 930, 1, 3)

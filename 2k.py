from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

# starting script
print "start"

# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
count = 1
while (count < 100):
    print "loop number: " + str(count)
    #start event
    print "entering into opponent selection"
    device.touch(500, 1100, MonkeyDevice.DOWN_AND_UP)
    time.sleep(5)

    #choose opponent
    print "choosing an opponent"
    device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    time.sleep(12)


    #selecting attribute
    print "choosing an attribute"
    device.touch(910, 1800, MonkeyDevice.DOWN_AND_UP)
    time.sleep(1)

    #1st player
    print "choosing 1st player"

    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    print "rapid clicking"
    for i in range(0, 10):
        time.sleep(1)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    print "waiting"
    time.sleep(2)

    #2nd player
    print "choosing 2nd player"
    device.touch(800, 1800, MonkeyDevice.DOWN_AND_UP)
    print "rapid clicking"
    for i in range(0, 10):
        time.sleep(1)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    print "waiting"
    time.sleep(2)
    #3rd player
    print "choosing 3rd player"
    device.touch(400, 1800, MonkeyDevice.DOWN_AND_UP)
    print "rapid clicking"
    for i in range(0, 10):
        time.sleep(1)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    print "waiting"
    time.sleep(2)
    #4th player
    print "choosing 4th player"
    device.touch(700, 1800, MonkeyDevice.DOWN_AND_UP)
    print "rapid clicking"
    for i in range(0, 10):
        time.sleep(1)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    print "waiting"
    time.sleep(2)
    #2nd player
    print "choosing 5th player"
    device.touch(200, 1800, MonkeyDevice.DOWN_AND_UP)
    print "rapid clicking"
    for i in range(0, 10):
        time.sleep(1)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
        device.touch(500, 1500, MonkeyDevice.DOWN_AND_UP)
    print "waiting"
    time.sleep(2)
    #clicking prize cars
    print "clicking cards"
    for i in range(0, 100):
        for j in range(20, 160):
            device.touch(i*10, j*10, MonkeyDevice.DOWN_AND_UP)
    time.sleep(1)
    #proceed back to beginning
    print "proceeding"
    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    device.touch(500, 1800, MonkeyDevice.DOWN_AND_UP)
    time.sleep(5)

    count +=1

print "end of script"

from __future__ import print_function
from __future__ import division

def monitorSensorthread():
    global distance
    while True:
        distance = my_distance_sensor.read_mm()



def drive():
    global deposit
    gpg.set_speed(300)

    if my_linefollower.read_position() == 'center':
        gpg.forward()
        global distance
        if distance <= 100:
            gpg.turn_degrees(180)
            gpg.forward()

    elif my_linefollower.read_position() == 'left':
        gpg.left()

    elif my_linefollower.read_position() == 'right':
        gpg.right()

    elif my_linefollower.read_position() == 'black':
        gpg.stop()
        time.sleep(5)
        deposit = False
        if deposit == False:
            #tähän servon pukkaaminen
            gpg.turn_degrees(180)
            gpg.forward()
            deposit = True
        
        
    elif my_linefollower.read_position() == 'endpoint' and deposit == True:
        gpg.stop()
        time.sleep(5)
        gpg.forward()
        deposit = False
        
    return

import threading
import easygopigo3 as easy
import time

distance = 0
deposit = True
driver = True
sensor_readings = None

gpg = easy.EasyGoPiGo3()

try:
    my_linefollower = gpg.init_line_follower()
    my_distance_sensor = gpg.init_distance_sensor()
    time.sleep(0.1)
except:
    print('Line Follower not responding')
    time.sleep(0.2)
    exit()
my_linefollower.read_position()
my_linefollower.read_position()
t = threading.Thread(target=monitorSensorthread)
t.start()

# start
#gpg.forward()
while driver == True:
    try:
        drive()
        print(deposit)

    except KeyboardInterrupt:
        print("Forced reset")
        gpg.reset_all()
        exit(0)

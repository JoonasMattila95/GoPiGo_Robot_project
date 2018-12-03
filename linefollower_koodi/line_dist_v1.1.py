#!/usr/bin/python3

from __future__ import print_function
from __future__ import division

def monitorSensorthread():
    global distance
    while True:
        distance = my_distance_sensor.read_mm()



def drive():
    global variable
    global old_variable
    global deposit
    gpg.set_speed(300)

    if my_linefollower.read_position() == 'center':
        gpg.forward()
        variable = 'center'
        
        global distance
        if distance <= 100:
            gpg.turn_degrees(180)
            gpg.forward()

    elif my_linefollower.read_position() == 'left':
        gpg.left()
        variable = 'left'

    elif my_linefollower.read_position() == 'right':
        gpg.right()
        variable = 'right'

    elif my_linefollower.read_position() == 'black':
        gpg.stop()
        time.sleep(2)
        if deposit == False:
            #tähän servon pukkaaminen
            GPG.set_servo(GPG.SERVO_2, 1000)
            gpg.turn_degrees(180)
            gpg.forward()
            deposit = True
        
        
    elif my_linefollower.read_position() == 'endpoint' and deposit == True:
        gpg.stop()
        variable = 'endpoint'
            
        time.sleep(2)
        gpg.forward()
        deposit = False
        
    if variable != '' and variable != old_variable:
        sql = "INSERT INTO ajodata (komento, timestamp) VALUES(%s, NOW())"
        cursor.execute(sql, variable)
        db.commit()
        old_variable = variable;
    
    return

import pymysql
import threading
import gopigo3
import easygopigo3 as easy
import time

db = pymysql.connect("localhost", "test_user", "test_password", "panttibotti"
)

cursor = db.cursor()

distance = 0
variable = ''
old_variable = ''
deposit = True
driver = True
sensor_readings = None

gpg = easy.EasyGoPiGo3()
GPG = gopigo3.GoPiGo3()

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

    except KeyboardInterrupt:
        print("Forced reset")
        gpg.reset_all()
        exit(0)

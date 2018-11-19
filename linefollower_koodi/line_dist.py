from __future__ import print_function
from __future__ import division


import easygopigo3 as easy
import time
import keyboard

sensor_readings = None
driver = True
s
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


# start
gpg.forward()

def drive():
    
    gpg.set_speed(200)
    
    if my_linefollower.read_position() == 'center':
        gpg.stop()
        distance = my_distance_sensor.read_mm()
        
        if distance <= 100:
            gpg.reset_all()
            driver = False
            print(driver)
            
        
    if my_linefollower.read_position() == 'left':
        gpg.left()
        
    if my_linefollower.read_position() == 'right':
        gpg.right()
        
    if my_linefollower.read_position() == 'black':
        gpg.right()
        
while driver == True:
    try:
        print(driver)
        drive()
        
    except KeyboardInterrupt: 
        gpg.reset_all()  
        exit(0)
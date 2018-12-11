from __future__ import print_function
from __future__ import division


def camera_thread():
   # while 1:
    global start
    global driver
    camera.capture('/home/pi/Desktop/GoPiGo3/Software/Python/cam.jpg')
    #print("camera threadissa")
        # Instantiates a client
    client = vision.ImageAnnotatorClient()

        # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname('__file__'),
        'cam.jpg')

        # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    if detect_text(file_name) == True:
        #print("uusi thread")
        start = True
        driver = True



        
def detect_text(path):
    #print("teksti threadi")
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        #print("tarkistus")
        p.pantti_tarkastus(text.description)

    if p.insertpantti() == True:     
        image_file.close
        return True
    else:
        image_file.close
        return False


def monitorSensorthread():
    global distance
    while True:
        distance = my_distance_sensor.read_mm()

def dropoff():
    servo.rotate_servo(5)
    time.sleep(0.5)
    servo.rotate_servo(110)
    return True

def drive():
    global deposit
    global start
    global driver
    global variable
    global old_variable
    #print("start %s",start)
    #print("driver %s",driver)
    gpg.set_speed(300)

    if my_linefollower.read_position() == 'center':
        gpg.forward()
        variable = 'center'
        global distance
        if distance <= 100 and distance != 0:
            gpg.set_speed(100)
            gpg.turn_degrees(180)

    elif my_linefollower.read_position() == 'left':
        gpg.left()
        variable = 'left'

    elif my_linefollower.read_position() == 'right':
        gpg.right()
        variable = 'right'

    elif my_linefollower.read_position() == 'black':
        gpg.stop()
        variable = 'endpoint'
        if deposit == False:
            if dropoff() == True:
                gpg.set_speed(100)
                gpg.turn_degrees(180)
                gpg.forward()
                deposit = True
              
    elif my_linefollower.read_position() == 'endpoint' and deposit == True:
        gpg.stop()
        variable = 'start'
        if start == True:
            gpg.forward()
            deposit = False
            start = False
        else:
            driver = False
    if variable != '' and variable != old_variable:
        p.insertajodata(variable)
        old_variable = variable
    return

import threading
import easygopigo3 as easy
import time
import threading
import io
import os
import pantti
import sys
from picamera import PiCamera
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/vision1-20f70600c2fc.json"
p = pantti.pantti(0,0)
camera = PiCamera()
camera.resolution = (2592, 1944)
#t1 = threading.Timer(1.0 , camera_thread)

variable = ''
old_variable = ''
distance = 0
start = False
deposit = True
driver = True
sensor_readings = None

gpg = easy.EasyGoPiGo3()

try:
    my_linefollower = gpg.init_line_follower()
    time.sleep(0.1)
except:
    print('Line Follower not responding')
    time.sleep(0.2)
    exit()

try:
    my_distance_sensor = gpg.init_distance_sensor()
    time.sleep(0.1)   
except:
    print('Distance sensor not responding')
    time.sleep(0.2)
    exit()

try:
    servo = gpg.init_servo()
    time.sleep(0.1)   
except:
    print('Servo not responding')
    time.sleep(0.2)
    exit()
    
my_linefollower.read_position()
my_linefollower.read_position()
t = threading.Thread(target=monitorSensorthread)

# start
#gpg.forward()
while True:
    if driver == True:
        try:
            if not t.isAlive():
                print("ajothreadi aloitus")
                t.start()
            drive()

        except KeyboardInterrupt:
            print("Forced reset")
            gpg.reset_all()
            sys.exit()
    elif driver == False:
        try:

            camera_thread()
            print("driver",driver)
            print("start",start)
            #if not t1.isAlive():
             #   print("threadi aloitus")
              #  t1.start()
               # print(start)
        except KeyboardInterrupt:
            print("Forced reset")
            gpg.reset_all()
            sys.exit()
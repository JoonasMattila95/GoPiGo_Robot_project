from __future__ import print_function
from __future__ import division


def camera_thread():
   # while 1:
    global start
    global driver
    camera.capture('/home/pi/Desktop/GoPiGo3/Software/Python/cam.jpg')
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
        start = True
        driver = True



        
def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        p.pantti_tarkastus(text.description)

    if p.insertpantti() == True:     
        image_file.close
        return True
    else:
        image_file.close
        return False

def monitorSocketConnections():
    global start
    global driver
    global Master
    while True:
        s.listen(1)
        c, addr = s.accept()
        print("got connection:",addr)
        while True:
            data = c.recv(BUFFER_SIZE)
            if not data: break
            if data == 'STOP':
                gpg.stop()
                gpg.reset_all()
                Master = False
                print('STOP')
            elif data == 'CONTINUE':
                print('CONTINUE')
                Master = True
            elif data == 'BYPASS':
                print('BYPASS')
                start = True
                driver = True
        c.close()
        
        
        
        

def monitorSensorthread():
    global distance
    while True:
        distance = my_distance_sensor.read_mm()

def dropoff():
    servo.rotate_servo(110)
    time.sleep(0.5)
    servo.rotate_servo(5)
    time.sleep(0.5)
    return True

def drive():
    global deposit
    global start
    global driver
    global variable
    global old_variable
    gpg.set_speed(300)

    if my_linefollower.read_position() == 'center':
        gpg.forward()
        variable = 'center'
        global distance
        if distance <= 100 and distance != 0:
            gpg.set_speed(200)
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
import socket
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

variable = ''
old_variable = ''
distance = 0
start = False
deposit = True
Master = True
driver = True
sensor_readings = None


s = socket.socket()
host = '192.168.43.81' #ip of raspberry pi
port = 5550
s.bind((host, port))
BUFFER_SIZE = 1024


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
t1 = threading.Thread(target=monitorSocketConnections)
t1.start()

# start
#gpg.forward()
while True:
    while Master == True:
        if driver == True:
            try:
                if not t.isAlive():
                    t.start()
                drive()

            except KeyboardInterrupt:
                gpg.reset_all()
                sys.exit()
        elif driver == False:
            try:

                camera_thread()

            except KeyboardInterrupt:
                gpg.reset_all()
                sys.exit()
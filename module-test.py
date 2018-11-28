def camera_thread():
    while 1:

        camera.capture('/etc/python2.7/pythonjutut/cam.jpg')

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
        detect_text(file_name)
        
def detect_text(path):
    """Detects text in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        pantti = p.pantti_tarkastus(text.description)

    p.pantti_tiedot()
    image_file.close

import re
import threading
import io
import os
from picamera import PiCamera
from google.cloud import vision
from google.cloud.vision import types
import pantti


try:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/pi/vision1-20f70600c2fc.json"
    p = pantti.pantti(0,0)
    camera = PiCamera()
    camera.resolution = (1600, 1200)
    t = threading.Thread(target=camera_thread)
    t.start()
except (KeyboardInterrupt, SystemExit):
    print("asd")
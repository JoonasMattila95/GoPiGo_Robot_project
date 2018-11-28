
def pantti(input_text):
    if input_text == "0,15":
        sum = sum + 0.15
        print(input_text)
        return 
    elif input_text == "0,20":
        sum = sum + 0.20
        print(input_text)       
    if input_text == "Pantti":
        print(input_text)
    elif input_text == "Pant":
        print(input_text)
        
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
      
        sum = pantti(text.description)

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        #            for vertex in text.bounding_poly.vertices])

#        print('bounds: {}'.format(','.join(vertices)))
    image_file.close
    
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
        
import threading
import io
import os
from picamera import PiCamera
from google.cloud import vision
from google.cloud.vision import types
camera = PiCamera()
camera.resolution = (1600, 1200)
t = threading.Thread(target=camera_thread)
t.start()

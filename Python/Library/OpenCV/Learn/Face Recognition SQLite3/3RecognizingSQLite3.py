# Last updated: Wed, March 03, 2021 - 22:35

"""
Step by step:
[x] Create dataset
[x] Train the recognizer
[~] Detector

Key:
~ :: CURRENT
x :: DONE
"""

import cv2 as cv
import numpy as np
import sqlite3

faceDetector = cv.CascadeClassifier('D:\Project\Github\Self\Hello-World-Of-Everything\Python\Library\OpenCV\Learn\src\haarcascade_frontalface_default.xml')


cameraman = cv.VideoCapture(0, cv.CAP_DSHOW)

recognizer = cv.face.LBPHFaceRecognizer_create()

# recognizer.load('Recognizer/trainedData.yml')
# In openCV 3.3 has removed load() and save(). load() is replaced with read() and save() is replaced with write()
recognizer.read('Recognizer/Training Data.yml')

def getProfileInfo(userID):
    connection = sqlite3.connect('User Database.db')
    sql = f'SELECT * FROM User WHERE ID = {userID}'
    pointer = connection.execute(sql)
    
    profile = None

    for row in pointer:
        profile = row
    connection.close()
    return profile

# font = cv.cv.InitFont(CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)
# Old version above

fontface = cv.FONT_HERSHEY_SIMPLEX
fontscale = 1.5
fontcolor = (0, 0, 0)
fontsize = 14

def FONT_Notes():
    '''
    # How to put text in the picture
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    fontscale = 1
    fontcolor = (255, 255, 255)
    cv2.putText(img, "PUT YOUR TEXT HERE", (x, y+h), fontface, fontscale, fontcolor) 
    '''
    # Reference: https://stackoverflow.com/questions/44021999/attributeerror-module-object-has-no-attribute-initfont
    # Example:
    '''
    cam = cv2.VideoCapture(0)

    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 255, 255)

    ret, im = cam.read()
    locy = int(im.shape[0]/2) # the text location will be in the middle
    locx = int(im.shape[1]/2) #           of the frame for this example

    while True:
        ret, im = cam.read()
        cv2.putText(im, "Success!", (locx, locy), fontFace, fontScale, fontColor) 
        cv2.imshow('im', im)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    '''
    pass

detected = False

while True:
    _, img = cameraman.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face = faceDetector.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in face:
        
        cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        
        userID, conf = recognizer.predict(gray[y:y+h,x:x+w])

        """
        SQLite3 get the user information
        """
        profile = getProfileInfo(userID)

        if profile != None:
            # In the cv2 api, images are arrays, so you don't need to convert fromarray
            cv.putText(img, str(profile[1]), (x, y+h), fontface, fontscale, fontcolor, thickness=2)
            cv.putText(img, str(profile[2]), (x, y+h+30), fontface, fontscale, fontcolor, thickness=2)
            cv.putText(img, str(profile[3]), (x, y+h+60), fontface, fontscale, fontcolor, thickness=2)
            cv.putText(img, str(x), (0, 30), fontface, fontscale, fontcolor, thickness=2)
            cv.putText(img, str(y), (0, 90), fontface, fontscale, fontcolor, thickness=2)

            if not detected:
                initial_x = x
                initial_y = y
                detected = True
            else:
                if initial_x - x > 100:
                    cv.putText(img, "Moved Left", (50, 50), fontface, fontscale, fontcolor, thickness=2)
            
    cv.imshow('Detecting face', img)

    if cv.waitKey(5) == ord('q'):
        break

cameraman.release()
cv.destroyAllWindows()
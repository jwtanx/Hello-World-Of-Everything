# Last updated: Sun, February 28, 2021 - 18:04

"""
Step by step:
[~] Create dataset
[ ] Train the recognizer
[ ] Detector

Key:
~ :: CURRENT
x :: DONE
"""

# Importing all the modules needed
import cv2 as cv
import os

# Creating a face detector
faceDetector = cv.CascadeClassifier('D:\Project\Github\Self\Hello-World-Of-Everything\Python\Library\OpenCV\Learn\src\haarcascade_frontalface_default.xml')

# Creating a cameraman to capture your face
cameraman = cv.VideoCapture(0, cv.CAP_DSHOW)

# Asking the user to enter their id [NOTE: MUST BE IN DIGIT]
while(True):
    try:
        ids = int(input('Enter your id in digit: '))
        break
    except:
        print('Please enter id in digit only!\n')

# Setting a folder name for your dataset folder
datasetFolderPath = 'Dataset'

# Setting the amount of face pic you want to save
totalImageNumber = 20

# Image number counter
imageNumber = 0

# Checking if a folder exists: https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/
if not os.path.exists(datasetFolderPath):
    print('Dataset folder not found, creating dataset folder...')
    os.mkdir(datasetFolderPath)
    print('Dataset folder created successfully.')

while(True):

    # Getting the cameraman to export the image
    _, img = cameraman.read()

    # Coverting the colored image into a gray version for easier work for the detector
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Detect the face from the gray photo
    face = faceDetector.detectMultiScale(gray, 1.3, 5)

    for x, y, w, h in face:
        # Save the image file (dataset)
        imageNumber += 1
        cv.imwrite(f"{datasetFolderPath}/{ids}_{imageNumber}.jpg", gray[y:y+h, x:x+w])
        """
        cv.imwrite(FILE_NAME, CROPPED_IMAGE_PIXEL)
        @param gray[y:y+h, x:x+w]: Capturing the part where your face is captured
        """

        # Drawing the rectangle for the user to see if their face is detected
        cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

        # Give it a 100ms before taking another photo
        cv.waitKey(100)

    # Showing the image with the rectangle drawn
    cv.imshow("Creating Face ID", img)

    # Adding some delay
    cv.waitKey(10)

    # We are not using the ord('q') this time, instead we use the if statement
    if imageNumber == totalImageNumber:
        break

print('Your face ID data is created. We will process it and recognize you soon.')

"""IMPORTANT"""
# Release the cameraman, don't let him overwork, unless you wanna pay more
cameraman.release()

# Shut the windows down before going home
cv.destroyAllWindows()

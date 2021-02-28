# Last updated: Sun, February 28, 2021 - 09:54

import cv2
import numpy as np

# Meaning of cascade here: arrange (a number of devices or objects) in a series or sequence
faceDectector = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')
catDetector = cv2.CascadeClassifier('src/haarcascade_frontalcatface.xml')

# Capturing video from our webcam
cap = cv2.VideoCapture(0)
# Alternative: cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
"""
Note:
I added cv2.CAP_DSHOW because I am getting this warning
[ WARN:1] global C:\..\videoio\src\cap_msmf.cpp (434) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback

# Ref: https://stackoverflow.com/questions/53888878/cv2-warn0-terminating-async-callback-when-attempting-to-take-a-picture/56839757#56839757
"""

# Caputuring the frame one by one in a while loop
while(1): # 1 == True
    ret, img = cap.read()
    """
    Return a tuple: ret & image
    @param ret: a value returned that check wether the reading was successful
    @param img: if the reading was successful, proceed using the image returned
    If you're not using the return value for anything, you can just set that portion to _, which tells Python "ignore me"

    # Ref: https://stackoverflow.com/questions/13989627/cv2-videocapture-read-does-not-return-a-numpy-array/13990546#13990546
    """

    # Converting the img to greyscale image because the image we now have is in colored image
    # And opencv need greyscale image to detect object
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvtColor = convert color from Blue Green Red to Gray

    # Now we can detect faces with the gray color match
    # This will detect all the faces in the color frame and return the coordinate of the face in the frame
    faces = faceDectector.detectMultiScale(gray, 1.3, 5)
    cats = catDetector.detectMultiScale(gray, 1.3, 5)
    """
    This will briefly detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles
    1st @param imageSource  : Pass in your image variable
    2nd @param scaleFactor  : Parameter specifying how much the image size is reduced at each image scale.
    3rd @param minNeighbors : Parameter specifying how many neighbors each candidate rectangle should have to retain it.

    For more optional paramaters:
    help(cv2.CascadeClassifier.detectMultiScale)
    """

    # Draw each and every face in every frame with a rectangle
    for (x, y, w, h) in faces:
        """
        @param x: position x
        @param y: position y
        @param w: width
        @param h: height
        """
        
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        """
        @param img: The source image
        @param pt1: Vertex of the rectangle. (Think of it like the top left coordinate of the face)
        @param pt2: Vertex of the rectangle opposite to pt1 . (Think of it like the bottom right coordinate of the face)
        @param color: Rectangle color or brightness (grayscale image). = (BlueVAL, GreenVAL, RedVAL)
        @param thickness: Thickness of lines that make up the rectangle. Negative values, like #FILLED,
        mean that the function has to draw a filled rectangle.

        For more optional parameters:
        help(cv2.rectangle)
        """
    for (x, y, w, h) in cats:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    # Showing the image
    cv2.imshow("Face", img)
    """
    imshow(winname, mat)
    @param winname: Windows name

    @note This function should be followed by cv::waitKey function which displays the image for specified
    milliseconds. Otherwise, it won't display the image. 
    For example, 
    **waitKey(0)** will display the window infinitely until any keypress (it is suitable for image display). 
    **waitKey(25)** will display a frame for 25 ms, after which display will be automatically closed.
    (If you put it in a loop to read videos, it will display the video frame-by-frame)
    """

    # Let's set it with 10ms delay and stop the loop if 'q' is pressed
    if (cv2.waitKey(10) == ord('q')):
        break

"""IMPORTANT"""
# We MUST release the camera
cap.release() # Closes video file or capturing device.

# We MUST destroy the windows
cv2.destroyAllWindows() # Destroys all of the HighGUI windows.

"""
Reference: https://www.youtube.com/watch?v=1Jz24sVsLE4
# Big thanks to Codacus
"""
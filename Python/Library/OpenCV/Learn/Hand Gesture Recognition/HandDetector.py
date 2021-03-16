# Last updated: Sun, February 28, 2021 - 10:44
# My way to remember how to OpenCV face detector
# Disclaimer: Nothing personal here. 

# Step 1: import cv2, the boss which is YOU
import cv2 as cv

# Step 2: 'Hire' a detector by cascading the classifier
faceDetector = cv.CascadeClassifier('D:\Project\Github\Self\Hello-World-Of-Everything\Python\Library\OpenCV\Learn\src\Extra\\palm.xml')

# Step 3: 'Hire' a cameraman
cameraman = cv.VideoCapture(0, cv.CAP_DSHOW)

# Step 4: Order your employee every single time
while(True):

    # Step 5: Order the cameraman to read the frame
    _, img = cameraman.read()

    # Step 6: Cut the cost, color is too expensive, convert the colored image into gray version
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Step 7: Order the faceDetector to detect the faces
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)

    # Step 8: Difficult part is done, now you do the 3-yo ezpz task
    for x, y, w, h in faces:
        cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

    # Step 9: Show off your the majestic drawings
    cv.imshow("Hand Detector", img)

    # Step 10: Setting up a backdoor to escape as the hiring fee is too expensive
    if (cv.waitKey(5) == ord('q')):
        break

# Step 11: Fire the cameraman
cameraman.release()

# Step 12: Shut your company down and tell the detector that you are broke so you don't need to pay muahahahaha
cv.destroyAllWindows()

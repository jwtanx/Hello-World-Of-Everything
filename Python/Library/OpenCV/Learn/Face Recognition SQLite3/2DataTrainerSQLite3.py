# Last updated: Sun, February 28, 2021 - 18:04

"""
Step by step:
[x] Create dataset
[~] Train the recognizer
[ ] Detector

Key:
~ :: CURRENT
x :: DONE
"""

# Importing all the modules needed 
import os, cv2 as cv, numpy as np
from PIL import Image

# Haiyaa, need to hire more employee, the recognizer
recognizer = cv.face.LBPHFaceRecognizer_create()

# Setting up the folder names
datasetFolderPath = 'Dataset'
recognizerFolderPath = 'Recognizer'

# Getting the faces in matrix form for training
def getImageFileList(directory):
    
    # Getting the relative path location
    imgPathList = [os.path.join(directory, f) for f in os.listdir(directory)]

    # Initializing the faces and ids list to store the data later
    faceNPs = []
    IDs = []

    for imgPath in imgPathList:

        faceImg = Image.open(imgPath).convert('L')
        """
        Image.convert(mode=None, matrix=None, dither=None, palette=0, colors=256)

        Dithering method, used when converting from mode “RGB” to “P” or from “RGB” or “L” to “1”.
        'L': Smooth img
        '1': More noise img

        Returns a converted copy of this image. For the “P” mode, this method translates pixels through the palette. If mode is omitted, a mode is chosen so that all information in the image and the palette can be represented without a palette.
        Ref: https://www.geeksforgeeks.org/python-pil-image-convert-method/
        """

        # @uint8: Unsigned Integers of 8 bits. A uint8 data type contains all whole numbers from 0 to 255.
        faceNP = np.array(faceImg, 'uint8')
        
        # Adding the array of the face into the list
        faceNPs.append(faceNP)
        
        ID = int(os.path.split(imgPath)[-1].split('_')[0])
        '''
        This one depends on your way of creating the images in step 1
        Just to extract the id, do change this if you have different image filename formatting previosuly
        For eg. user_555_2.jpg -> We just want the 555, the id
        '''

        # Adding the id to the ID list
        IDs.append(ID)

        # Showing the faces of each of the image created while training it
        cv.imshow('Training in progress...', faceNP)
        cv.waitKey(10)

    print('Training completed!')
    return faceNPs, IDs

# Getting the list of the faces and the list of the ids
faces, ids = getImageFileList(datasetFolderPath)

# Give in-house training to the recognizer you hired and tell them the output for each of the image shown
recognizer.train(faces, np.array(ids))

# Recognizer try to find a notebook page to jot down his/her notes
if not os.path.exists(recognizerFolderPath):
    os.mkdir(recognizerFolderPath)

# Recognizer save the notes in the notebook
recognizer.save(f'{recognizerFolderPath}/Training Data.yml')

# Time to go home, out of office hour now
cv.destroyAllWindows()
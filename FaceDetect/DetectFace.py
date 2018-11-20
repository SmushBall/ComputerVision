# Author: Deepak Kumar Singh
# Date : 05/Aug/2018 
# This program detects faces in a given image using OpenCV.


import cv2
import sys

# Get the input image
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create and initialize the cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image and convert to grayscale
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image with function detectMultiScale on face cascade
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

# Display the number of faces found
print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces found
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with recatangles near the faces
cv2.imshow("Faces found", image)
cv2.waitKey(0)

# Author: Deepak Kumar Singh
# Date: 06/Aug/2018
# This program detects a face on a webcam using OpenCV

import cv2
import sys
import logging as log
import datetime as dt 
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
# log.basicConfig(filename = 'webcam.log', level='log.info')

video_capture = cv2.VideoCapture(0)
anterior = 0
ramp_frames = 30

def get_image():
	ret, im = video_capture.read()
	return im

while True:
    if not video_capture.isOpened():
    	print("Unable to Load Camera.")
    	sleep(5)
    	pass


    for i in range(ramp_frames):
	    frame1 = get_image()

    print("Taking image...")
    frame = get_image()


    # Capture frame by frame
    #ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale (
    	gray,
    	scaleFactor = 1.1,
    	minNeighbors = 5,
    	minSize = (30,30)
    )	

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
    	cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)


   # if anterior != len(faces):
   #     anterior = len(faces)
    #    log.info("faces: " + str(len(faces))+ " at "+ str(dt.datetime.now()))	

    # Display the resulting frame
    cv2.imshow('video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('video', frame)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()        
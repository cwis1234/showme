import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
import glob

face_cascade = cv2.CascadeClassifier('D:/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')


images = glob.glob('D:/woman/*.png')
print(len(images))

for image in images:
    img = cv2.imread(image)
    grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayImage,1.03,5)
    if len(faces) == 0:
        os.remove(image)
        continue
    print(image)
    print("Number of faces detected: " + str(faces.shape[0]))
    if faces.shape[0] != 1:
        os.remove(image)
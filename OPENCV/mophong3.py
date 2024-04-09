import numpy as np
import cv2

ch= 19
khoangcachthuc = 45

CascadeClass = cv2.CascadeClassifier('D:\CODE\OPENCV\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def detecFace(img):
    chieurong = 0
    BGRgray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    khuonmat =  CascadeClass.detecMultiScale(BGRgray)
    for mat in khuonmat:
        a, b, c, d = mat
        cv2.rectangle(img, (a,b), (a+c, b+d), (255, 255, 0), 3)
        chieurong = c
    return chieurong

img = cv2.imread('WIN_20230421_16_13_50_Pro.jpg')
in_Chieurong = detecFace(img)
tieucu = (in_Chieurong*khoangcachthuc)/ch
print(tieucu)
cv2.inshow("Image", img)

while True:
    r, photo = cap.read()
    Chieurongs = detecFace(photo)

    if Chieurongs != 0:
        cv2.putText(photo, "Khoang cach: ", (5, 20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,255), 2)
        khoangcach = (tieucu*khoangcach)/Chieurongs
        khoangcach = round(khoangcach, 2)

        cv2.putText(photo, "DON VI CM: "+str(khoangcach), (20,20), cv2.FONT_HERSHEY_DUPLEX, 0.8, (192, 128, 0), 2)
    cv2.imshow('WebCamDell', photo)
    cv2.waitKey(1)
        
    

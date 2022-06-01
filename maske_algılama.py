# -*- coding: utf-8 -*-
import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")

org = (30,40)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1


cap = cv2.VideoCapture(0)
img = cv2.imread('Resim1.jpg')

face = face_cascade.detectMultiScale(img, 1.05, 7)

weared_mask = "Maske taktiginiz icin tesekkurler"
not_weared_mask = "Lutfen maske takiniz!!"
if(len(face) == 0):
    cv2.putText(img, "Yuz bulunamadi!!", org, fontFace, fontScale, (255,255,255), 2)
else:
    for x, y, w, h in face:
        roi_gray = img[y:y+h, x:x+w]
        
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.4, 15)
        
        if(len(mouth) == 0): 
            cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0), 2)
            cv2.putText(img, weared_mask,(x,y), fontFace,fontScale, (0,255,0), 2, cv2.LINE_AA)
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255), 2)
            cv2.putText(img, not_weared_mask, (x,y),fontFace, fontScale, (0,0,255), 2, cv2.LINE_AA)
            for mx, my, mw, mh in mouth:
                cv2.rectangle(img, (mx+x,my+y), (mx+x+mw, my+y+mh), (0,0,255),3)
                        
cv2.imshow("Mask Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()




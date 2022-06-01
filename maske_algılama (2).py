# -*- coding: utf-8 -*-
import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml")

org = (30,40)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kamera açılamadı!!")
        
    gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray_image, 1.05, 7)
    weared_mask = "Maske taktiginiz icin tesekkurler"
    not_weared_mask = "Lutfen maske takiniz!!"
    if(len(faces) == 0):
        cv2.putText(frame, "Yuz bulunamadi!!", org, fontFace, fontScale, (255,255,255), 2)
    else:
        for x, y, w, h in faces:
            roi_gray = gray_image[y:y+h, x:x+w]
            
            mouth = mouth_cascade.detectMultiScale(roi_gray, 1.4, 15)
            
            if(len(mouth) == 0): 
                cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0), 2)
                cv2.putText(frame, weared_mask,(x,y), fontFace,fontScale, (0,255,0), 2, cv2.LINE_AA)
            else:
                cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255), 2)
                cv2.putText(frame, not_weared_mask, (x,y),fontFace, fontScale, (0,0,255), 2, cv2.LINE_AA)
                for mx, my, mw, mh in mouth:
                    cv2.rectangle(frame, (mx+x,my+y), (mx+x+mw, my+y+mh), (0,0,255),3)
                            
    resize = cv2.resize(frame,(1000,800))
    cv2.imshow("Mask Detection",resize)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("by")
        break

cap.release()
cv2.destroyAllWindows()



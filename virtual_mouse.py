import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np
import time
cap = cv2.VideoCapture(0)


cap.set(3,640)

cap.set(4,480)
pTime = 0
detector = HandDetector(detectionCon=0.8,maxHands=1)
while True:
    success, img = cap.read()
    hands,img = detector.findHands(img,flipType=True)
    if hands:
        hand1=hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        x1=lmList1[8][0]
        y1=lmList1[8][1]
        x2=lmList1[12][0]
        y2=lmList1[12][1]
        #print(x1,y1,x2,y2)
        fingers1 = detector.fingersUp(hand1)
        #print(fingers1)
        if fingers1[1]==1 and fingers1[2]==0:
            x3 = np.interp(x1,(0,640),(0,1365))
            y3 = np.interp(y1,(0,480),(0,767))
            print(x3,y3)
            pyautogui.moveTo(x3,y3)
        #if fingers1[2]==1:
            #pyautogui.click()
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    
    cv2.imshow("Image",img)
    
    cv2.waitKey(1)
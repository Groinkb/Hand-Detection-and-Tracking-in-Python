import cv2
import mediapipe as mp 

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils


webcam = cv2.VideoCapture(0)
while webcam.isOpened():
    success, img = webcam.read()

    results=mp_hands.Hands().process(img)


    cv2.imshow('Koolac', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
               break
webcam.release()

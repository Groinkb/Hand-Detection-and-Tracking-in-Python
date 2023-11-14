import cv2
import mediapipe as mp 

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils


webcam = cv2.VideoCapture(0)
while webcam.isOpened():
    success, img = webcam.read()
    

    #applying hand tracking model with cv
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=mp_hands.Hands().process(img)


    #draw annotations on the image 
    img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks: 
            for hand_landsmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(img,hand_landsmarks,mp_hands.HAND_CONNECTIONS)


    cv2.imshow('Koolac', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
               break
webcam.release()
cv2.destroyAllWindows()

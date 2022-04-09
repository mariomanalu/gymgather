import cv2
import mediapipe as mp
import numpy as np
import matplotlib as mpl
import face_recognition
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# VIDEO FEED
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    rgb_frame = frame[:,:,::-1]

    face_locations = face_recognition.face_locations(rgb_frame, model = "hog")

    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
    cv2.imshow('Mediapipe Feed', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
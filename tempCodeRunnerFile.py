import pickle
import cv2
import numpy as np
import time
import os
import csv
from datetime import datetime
from sklearn.neighbors import KNeighborsClassifier
from win32com.client import Dispatch

def speak(text):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)

with open('data/faces_data.pkl', 'rb') as f:
    faces_data = pickle.load(f)

with open('data/names.pkl', 'rb') as w:
    names = pickle.load(w)

if len(faces_data) != len(names):
    if len(faces_data) < len(names):
        names = names[:len(faces_data)]
    else:
        faces_data = faces_data[:len(names)]


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(faces_data, names)

with open('data/knn_model.pkl', 'wb') as model_file:
    pickle.dump(knn, model_file)

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

imgBackground = cv2.imread("background.png")

COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        
        output = knn.predict(resized_img)
        
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        
        exist = os.path.isfile(f"Attendance/Attendance_{date}.csv")
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        
        attendance = [str(output[0]), str(timestamp)]
        
        imgBackground[162:162 + 480, 55:55 + 640] = frame
        cv2.imshow("Frame", imgBackground)

    k = cv2.waitKey(1)
    if k == ord('o'):
        speak("Attendance Taken..")
        time.sleep(5)
        
        if exist:
            with open(f"Attendance/Attendance_{date}.csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open(f"Attendance/Attendance_{date}.csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
    
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
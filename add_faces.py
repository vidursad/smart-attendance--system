import cv2
import pickle
import numpy as np
import os

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

faces_data = []
i = 0
name = input("Enter Your Name: ")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50))

        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
        i = i + 1

        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    k = cv2.waitKey(1)
    if k == ord('q') or len(faces_data) == 100:
        break

video.release()
cv2.destroyAllWindows()

faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)  

if 'names.pkl' not in os.listdir('data/'):
    names = [name] * 100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 100
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)

# Load existing faces_data.pkl or create a new one
faces_file_path = 'data/faces_data.pkl'

if not os.path.exists(faces_file_path):
    with open(faces_file_path, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open(faces_file_path, 'rb') as f:
        faces = pickle.load(f)

    # Ensure faces is a NumPy array and reshape if necessary
    faces = np.array(faces)  # Convert list to array if needed

    if faces.ndim == 1:  # Reshape if it's wrongly stored as 1D
        faces = faces.reshape(-1, faces_data.shape[1])

    print(f"Shape of faces before merging: {faces.shape}")
    print(f"Shape of new faces_data: {faces_data.shape}")

    # Ensure both arrays have the same feature size before stacking
    if faces.shape[1] == faces_data.shape[1]:
        faces = np.vstack([faces, faces_data])  # Merge new data
    else:
        print("Error: Shape mismatch between faces and faces_data!")
        exit()

    # Save the updated data
    with open(faces_file_path, 'wb') as f:
        pickle.dump(faces, f)

print("Faces data saved successfully!")

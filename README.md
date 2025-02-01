# Smart Attendance System Using Face Recognition

## Introduction
The Smart Attendance System is an AI-powered application that automates attendance tracking using face recognition. This eliminates the need for manual attendance marking, making the process more efficient, accurate, and secure. The system uses OpenCV for image processing, KNN for face recognition, and Streamlit for the user interface.
<br /><br />
![Screenshot (140)](https://github.com/user-attachments/assets/e19fd3b6-503b-4112-bfbe-84c99d12bd81)

## Features
Automated Attendance Tracking – No manual input required.<br />
Face Recognition – Uses a trained model for accurate detection.<br />
Web-Based Interface – Built using Streamlit for ease of use.<br />
Data Logging – Stores attendance records in CSV format for future reference.<br />
Real-Time Processing – Captures live video feed for facial recognition.

## Technologies & Libraries Used and there purpose
Python         :     Core programming language <br />
OpenCV         :     Image processing and face detection <br />
KNN Algorithm  :     Face recognition model <br />
Streamlit      :     Web-based user interface <br />
NumPy          :     Numerical operations <br />
Pandas         :     Data handling and CSV file management

## Installation
Ensure you have Python installed (>= 3.7). Then, install the required dependencies using:
#### pip install opencv-python streamlit numpy pandas
<br />

## Project Workflow


### 1. Data Collection
Capture images of individuals using OpenCV.
Store multiple images per person for accurate recognition.
### 2. Face Detection & Feature Extraction
OpenCV detects faces in images.<br />
Extracts facial features and stores them for recognition.

![Screenshot (146)](https://github.com/user-attachments/assets/bc36e9b0-42bd-410c-95ba-baeab54919d1)
### 3. Training Model Using KNN
K-Nearest Neighbors (KNN) algorithm is used for classifying faces.<br />
Model is trained using labeled facial data.
### 4. Real-Time Face Recognition
The system captures live video input.<br />
Compares detected faces with the trained dataset.<br />
If a face is recognized, attendance is marked.
### 5. Attendance Taken
Attendance is recorded in a CSV file with timestamps.<br />
The stored file can be used for reporting and can be shown using streamlit on server.

![Screenshot (148)](https://github.com/user-attachments/assets/a8569031-efdd-4d35-a560-2cc3ba52f0f5)

## Usage
1.Run the application using the following command:
#### streamlit run app.py
2.Upload new images to register individuals.
3.Start live face recognition for attendance marking.
4.View or export attendance records in CSV format.

## Future Enhancements
1.Improve accuracy using deep learning models (e.g., CNN, FaceNet).<br />
2.Add cloud storage for attendance records.<br />
3.Implement multi-camera support for large organizations.<br />
4.Mobile app integration for remote attendance.

## Contributors

### Vidur Sad – Developer
![Screenshot (147)](https://github.com/user-attachments/assets/799a489f-51ff-4037-a017-13c9966d0ca7)
![Screenshot (137)](https://github.com/user-attachments/assets/d600d7bd-8c3e-481b-903c-9110bbe575b6)
![Screenshot (144)](https://github.com/user-attachments/assets/9ac75303-cbab-4b12-86e0-760584ef010f)
![Screenshot (141)](https://github.com/user-attachments/assets/a11c90f8-f249-4bf1-bbdf-8a848f837e93)

# Smart Attendance System Using Face Recognition

## Introduction
The Smart Attendance System is an AI-powered application that automates attendance tracking using face recognition. This eliminates the need for manual attendance marking, making the process more efficient, accurate, and secure. The system uses OpenCV for image processing, KNN for face recognition, and Streamlit for the user interface.

## Features
Automated Attendance Tracking – No manual input required.
Face Recognition – Uses a trained model for accurate detection.
Web-Based Interface – Built using Streamlit for ease of use.
Data Logging – Stores attendance records in CSV format for future reference.
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

## Project Workflow

### 1. Data Collection
Capture images of individuals using OpenCV.
Store multiple images per person for accurate recognition.
### 2. Face Detection & Feature Extraction
OpenCV detects faces in images.<br />
Extracts facial features and stores them for recognition.
### 3. Training Model Using KNN
K-Nearest Neighbors (KNN) algorithm is used for classifying faces.<br />
Model is trained using labeled facial data.
### 4. Real-Time Face Recognition
The system captures live video input.<br />
Compares detected faces with the trained dataset.<br />
If a face is recognized, attendance is marked.
### 5. Attendance Logging
Attendance is recorded in a CSV file with timestamps.<br />
The stored file can be used for reporting.

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

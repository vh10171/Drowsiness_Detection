# 💤 Real-Time Drowsiness Detection System

A real-time drowsiness detection system using **Python**, **OpenCV**, and **Mediapipe** that monitors eye movements and alerts the user if they appear drowsy.

## 🔍 How It Works

This system uses:
- **Mediapipe FaceMesh** to detect facial landmarks.
- **Eye Aspect Ratio (EAR)** to calculate eye openness.
- An alert is triggered (beep + warning text) if eyes remain closed for a few seconds, indicating possible drowsiness.

## 📸 Features

- Real-time face and eye tracking from webcam
- Calculates EAR for both eyes
- Detects drowsiness based on EAR threshold and duration
- Audio + visual alert if drowsiness is detected

## 🧠 Technologies Used

- Python
- OpenCV
- Mediapipe
- NumPy
- winsound (for Windows alert sound)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vh10171/drowsiness-detection.git
   cd drowsiness-detection

📬 Contact
Feel free to connect on LinkedIn or message me for collaboration!   
   


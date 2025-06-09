import cv2
import mediapipe as mp
import time
import numpy as np
import winsound

# Initialize Mediapipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)

# Define eye landmarks (left and right eyes)
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# EAR calculation
def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def calculate_ear(eye):
    vertical1 = euclidean(eye[1], eye[5])
    vertical2 = euclidean(eye[2], eye[4])
    horizontal = euclidean(eye[0], eye[3])
    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

# Webcam input
cap = cv2.VideoCapture(0)

sleep_start = None
DROWSY_THRESHOLD = 0.25
DURATION_THRESHOLD = 3  # seconds

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            landmarks = [(int(lm.x * w), int(lm.y * h)) for lm in face_landmarks.landmark]

            left_eye = [landmarks[i] for i in LEFT_EYE]
            right_eye = [landmarks[i] for i in RIGHT_EYE]

            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0

            if avg_ear < DROWSY_THRESHOLD:
                if sleep_start is None:
                    sleep_start = time.time()
                elif time.time() - sleep_start > DURATION_THRESHOLD:
                    winsound.Beep(1000, 500)
                    cv2.putText(frame, "DROWSINESS ALERT!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            else:
                sleep_start = None

            # Draw eyes
            for point in left_eye + right_eye:
                cv2.circle(frame, point, 2, (0, 255, 0), -1)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

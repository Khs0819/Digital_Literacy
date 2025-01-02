import cv2
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import joblib



base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options,
                                       num_hands=1)
detector = vision.HandLandmarker.create_from_options(options)

MARGIN = 10  
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)
PREDICTED_LABEL_COLOR = (0, 0, 255)

def draw_landmarks_on_image(rgb_image, detection_result, predicted_label):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list = detection_result.handedness
    annotated_image = np.copy(rgb_image)

    for idx in range(len(hand_landmarks_list)):
        hand_landmarks = hand_landmarks_list[idx]
        handedness = handedness_list[idx]

        hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            hand_landmarks_proto,
            solutions.hands.HAND_CONNECTIONS,
            solutions.drawing_styles.get_default_hand_landmarks_style(),
            solutions.drawing_styles.get_default_hand_connections_style())

        height, width, _ = annotated_image.shape
        x_coordinates = [landmark.x for landmark in hand_landmarks]
        y_coordinates = [landmark.y for landmark in hand_landmarks]
        text_x = int(min(x_coordinates) * width)
        text_y = int(min(y_coordinates) * height) - MARGIN

        cv2.putText(annotated_image, f"{handedness[0].category_name}",
                    (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

        cv2.putText(annotated_image, f"Predicted: {predicted_label}",
                    (text_x, text_y + 30), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, PREDICTED_LABEL_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    return annotated_image


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    detection_result = detector.detect(mp_image)

    hand_landmarks_list = detection_result.hand_landmarks
    if hand_landmarks_list:
        data = []
        for i in range(len(hand_landmarks_list[0])):
            landmark = hand_landmarks_list[0][i]
            data.extend([landmark.x, landmark.y, landmark.z])
        data = np.array(data).reshape(1, -1)
        predicted_label = rf_classifier.predict(data)

        annotated_image = draw_landmarks_on_image(rgb_frame, detection_result, predicted_label[0])

        bgr_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)

        cv2.imshow('Camera Feed', bgr_annotated_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

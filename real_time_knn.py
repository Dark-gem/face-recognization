import dlib
import cv2
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

# Load the pre-trained face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmarks model from dlib
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Load the pre-trained face recognition model from dlib
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Load the pre-trained KNN model for face identification
with open('knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)


# Function to extract 128-dimensional features from a face
def extract_face_features(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    # Iterate over detected faces
    face_features = []
    for face in faces:
        # Predict facial landmarks for the detected face
        shape = predictor(gray, face)

        # Calculate the 128-dimensional face features
        features = np.array(facerec.compute_face_descriptor(image, shape))
        face_features.append(features)

    return faces, face_features


# Function to identify faces using the KNN model
def identify_faces(face_features):
    # Prepare an empty list to store the predicted labels and confidence scores
    labels = []
    confidences = []

    # Iterate over the face features
    for features in face_features:
        # Reshape the features for prediction
        features = features.reshape(1, -1)

        # Predict the label using the KNN model
        distances, indices = knn_model.kneighbors(features, n_neighbors=1)
        min_distance = distances[0][0]

        # Calculate the confidence level as a percentage
        confidence = (1 - min_distance) * 100

        # Set a threshold of 0.6
        if min_distance <= 0.6:
            label = knn_model.classes_[indices[0][0]]
        else:
            label = "Unknown"

        # Append the predicted label and confidence to the lists
        labels.append(label)
        confidences.append(confidence)

    return labels, confidences


# Capture video from the default camera
cap = cv2.VideoCapture(0)

# ... (previous code)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    if not ret:
        # If the frame is empty, break the loop
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract facial features from the frame
    faces, face_features = extract_face_features(frame)

    if len(faces) > 0:
        # Identify the faces using the KNN model
        labels, confidences = identify_faces(face_features)

        # Iterate over the detected faces, their corresponding labels, and confidences
        for face, label, confidence in zip(faces, labels, confidences):
            # Extract the coordinates of the bounding box
            (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())

            # Display the label and confidence on top of the bounding boxb
            label_text = f'{label} ({confidence:.2f}%)'
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Identification', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()

import cv2

def recognize_faces(label_dict):
    # Load the face recognizer and the face detector
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_trainer.yml")

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # Recognize the face
            roi_gray = gray[y:y+h, x:x+w]
            id_, confidence = recognizer.predict(roi_gray)

            # Check if the recognition is confident
            if confidence < 100:
                name = label_dict[id_]
                confidence_text = f"{round(100 - confidence)}%"
            else:
                name = "Unknown"
                confidence_text = "N/A"

            # Display the name and confidence
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            cv2.putText(frame, confidence_text, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the resulting frame
        cv2.imshow('Recognize Faces', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

recognize_faces({0: '1002', 1: '1001'})
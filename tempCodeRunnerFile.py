import cv2
import mysql.connector

def face_recog(self):
    def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        if img is None:  # Check if the image is empty
            print("Error: Image not captured")
            return []

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            # Connect to MySQL database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="8040face", database="face_recognizer")
            my_cursor = conn.cursor()

            # Fetch student data using parameterized query to prevent SQL injection
            my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (id,))
            n = my_cursor.fetchone()
            n = "+".join(map(str, n)) if n else "Unknown"  # Handle None case

            my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (id,))
            r = my_cursor.fetchone()
            r = "+".join(map(str, r)) if r else "Unknown"

            my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (id,))
            d = my_cursor.fetchone()
            d = "+".join(map(str, d)) if d else "Unknown"

            # If the confidence is greater than 77, display the recognized information
            if confidence > 77:
                cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
            else:
                # If confidence is less than 77, mark as unknown
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            # Store coordinates of the face (optional if needed later)
            coord = [x, y, w, h]

        return coord

    def recognize(img, clf, faceCascade):
        coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img

    # Load the face cascade and the pre-trained classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    # Open the webcam
    video_cap = cv2.VideoCapture(0)

    while True:
        ret, img = video_cap.read()

        # Check if frame was captured successfully
        if not ret:
            print("Error: Failed to capture image")
            break

        img = recognize(img, clf, faceCascade)

        # Display the result
        cv2.imshow("Welcome To Face Recognition", img)

        # Break the loop if the Enter key (13) is pressed
        if cv2.waitKey(1) == 13:
            break

    # Release the webcam and close the window
    video_cap.release()
    cv2.destroyAllWindows()

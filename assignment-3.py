import os
import cv2
import numpy as np

if __name__ == "__main__":

    # Capture frames from webcam
    vid = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Video writer speciications
    output_filepath = "vid_face_detect.mp4"
    ret, frame = vid.read()
    frame_size = (frame.shape[1], frame.shape[0])
    fps = 20
    count = 0
    output = cv2.VideoWriter(
        output_filepath, cv2.VideoWriter_fourcc(*"XVID"), fps, frame_size
    )

    # Event loop to capture frames from webcam
    while True:
        ret, frame = vid.read()

        # Display the resulting frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30)
        )

        # Draw text and bbox
        cv2.putText(
            frame,
            str(count),
            (frame.shape[1] - 50, 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            [225, 255, 255],
            thickness=2,
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + h, y + h), (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

        # Dump frames to disk
        output.write(frame)

        count += 1

    vid.release()
    output.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

import os

import cv2

from PR3 import rescale_image
from PR1 import image_folder

capture = cv2.VideoCapture(os.path.join(image_folder, "vid1.mp4"))

while True:
    frame_loaded, frame = capture.read()

    if frame is not None:
        frame_rescaled = rescale_image(frame, 0.5)
        cv2.imshow('Original', frame)
        cv2.imshow('Rescaled', frame_rescaled)
    else:
        print("Frame is not captured")
        exit(1)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)



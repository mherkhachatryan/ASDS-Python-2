import cv2

capture = cv2.VideoCapture('./img/vid1.mp4')

while True:
    frame_loaded, frame = capture.read()

    if frame_loaded:
        cv2.imshow("vid1", frame)
    else:
        print("Empty Frame")
        exit(1)

    if cv2.waitKey(20) & 0xFF == ord('1'):
        break

capture.release()
cv2.destroyAllWindows()

cv2.waitKey(0)



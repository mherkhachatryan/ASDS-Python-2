import cv2

from PR5 import image, image_original

if __name__ == "__main__":
    cv2.rectangle(image, (20,20), (200, 200), (17, 132, 240), thickness=2)

    cv2.imshow('Rectangle', image)
    cv2.imshow("Original", image_original)

    cv2.waitKey(0)


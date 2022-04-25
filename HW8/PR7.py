import cv2

from PR5 import image, image_original

if __name__ == "__main__":
    cv2.line(image, (image.shape[0], 0), (0, image.shape[1]), (0, 255, 0), thickness=3)
    cv2.imshow('Line', image)
    cv2.imshow("Original", image_original)
    cv2.waitKey(0)


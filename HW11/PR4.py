import cv2
import numpy as np

from PR1 import second_image_name, second_image_path

if __name__ == "__main__":
    img = cv2.imread(second_image_path)
    cv2.imshow(second_image_name, img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(gray, cv2.CV_64F)  # matrix value type float 64
    lap = np.uint8(np.absolute(lap))

    cv2.imshow('laplacian', lap)

    # maybe better way
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0)
    blur_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    sobel = cv2.Canny(blur_gray, threshold1=100, threshold2=200)

    cv2.imshow('Canny', sobel)
    cv2.waitKey(0)

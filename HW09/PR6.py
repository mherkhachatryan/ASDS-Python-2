import cv2
import numpy as np

from PR1 import third_image_name, third_image_path

if __name__ == "__main__":
    img = cv2.imread(third_image_path)
    cv2.imshow(third_image_name, img)
    blank_canny = np.zeros(img.shape, dtype='uint8')
    blank_gray_blurred = blank_canny.copy()

    canny = cv2.Canny(img, 125, 175)

    contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(blank_canny, contours, -1, (0, 0, 255), 1)
    cv2.imshow("contours_canny_on_original", blank_canny)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blured_gray = cv2.GaussianBlur(gray, (7, 7), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blured_gray, 125, 255, cv2.THRESH_BINARY)

    contours_blured, hierarchies_blured = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(blank_gray_blurred, contours_blured, -1, (0, 0, 255), 1)
    cv2.imshow("contrours_blurred_gray", blank_gray_blurred)

    cv2.waitKey(0)

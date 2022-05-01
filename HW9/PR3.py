import cv2

from PR1 import second_image_name, second_image_path

if __name__ == "__main__":

    img = cv2.imread(second_image_path)

    canny = cv2.Canny(img, 125, 175)
    cv2.imshow("cany", canny)
    cv2.imshow(second_image_name, img)

    img_blur_11 = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)
    canny_blured = cv2.Canny(img_blur_11, 125, 175)

    cv2.imshow("canny blurred", canny_blured)

    cv2.waitKey(0)

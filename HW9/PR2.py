import cv2

from PR1 import first_image_path, first_image_name

if __name__ == "__main__":
    img = cv2.imread(first_image_path)

    img_blur_3 = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)

    img_blur_11 = cv2.GaussianBlur(img, (11, 11), cv2.BORDER_DEFAULT)

    cv2.imshow(first_image_name, img)
    cv2.imshow("blur 3", img_blur_3)
    cv2.imshow("blur 11", img_blur_11)

    cv2.waitKey(0)

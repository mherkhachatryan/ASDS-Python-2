import cv2

from PR1 import second_image_name, second_image_path

if __name__ == "__main__":
    img = cv2.imread(second_image_path)
    cv2.imshow(second_image_name, img)

    img_resize_width = cv2.resize(img, (img.shape[0], img.shape[1]*2), interpolation=cv2.INTER_AREA)
    img_resize_height = cv2.resize(img, (img.shape[0]//2, img.shape[1]), interpolation=cv2.INTER_CUBIC)

    cv2.imshow("img_resize_width", img_resize_width)
    cv2.imshow("img_resize_height", img_resize_height)

    cv2.waitKey(0)

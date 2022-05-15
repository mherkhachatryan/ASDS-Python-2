import cv2

from PR1 import first_image_path, first_image_name

if __name__ == "__main__":
    img = cv2.imread(first_image_path)
    cv2.imshow(first_image_name, img)

    b, g, r = cv2.split(img)

    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    cv2.imshow('red', r)

    cv2.waitKey(0)

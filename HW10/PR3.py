import cv2

from PR1 import second_image_name, second_image_path

if __name__ == "__main__":
    img = cv2.imread(second_image_path)
    cv2.imshow(second_image_name, img)

    average = cv2.blur(img, (7, 7))

    cv2.imshow('average blur', average)

    bilateral1 = cv2.bilateralFilter(img, 5, 15, 15)

    cv2.imshow('bilateral1', bilateral1)

    bilateral2 = cv2.bilateralFilter(img, 5, 100, 15)
    cv2.imshow('bilateral2', bilateral2)

    # For this parameters bilateral2 edges are more blured than in bilateral1
    
    cv2.waitKey(0)


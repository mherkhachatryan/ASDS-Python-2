import cv2
import numpy as np

from PR1 import second_image_name, second_image_path

if __name__ == "__main__":
    img = cv2.imread(second_image_path)
    cv2.imshow(second_image_name, img)

    black_image = np.zeros(img.shape[:2], dtype=np.uint8)

    circle = cv2.circle(black_image.copy(), (img.shape[1] // 2, img.shape[0] // 2),
                        70, 255, thickness=-1)

    result = cv2.bitwise_and(img, img, mask=circle)

    cv2.imshow("result", result)

    cv2.waitKey(0)

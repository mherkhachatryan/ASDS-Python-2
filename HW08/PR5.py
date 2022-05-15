import cv2

from PR1 import file_paths

image = cv2.imread(file_paths[1])
image_original = image.copy()

if __name__ == "__main__":
    cv2.circle(image, (200, 200), 50, (0, 255, 0), thickness=3)

    cv2.imshow('Circle', image)
    cv2.imshow("Original", image_original)

    cv2.waitKey(0)

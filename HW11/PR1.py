from pathlib import Path
import os

import cv2
import matplotlib.pyplot as plt


img_files = os.path.join(Path(__file__).parent.absolute(), "img")

first_image_path = os.path.join(img_files, "pic1.jpg")
first_image_name = first_image_path.strip(".jpg").split("/")[-1]

second_image_path = os.path.join(img_files, "pic2.jpg")
second_image_name = first_image_path.strip(".jpg").split("/")[-1]

if __name__ == "__main__":
    img = cv2.imread(first_image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plt.imshow(gray)
    plt.show()

    plt.hist(gray.ravel(), 256, [0, 256])
    plt.xlabel("Pixel values")
    plt.ylabel("log(# of pixels)")
    plt.yscale("log")  # to make visually interpretable
    plt.show()



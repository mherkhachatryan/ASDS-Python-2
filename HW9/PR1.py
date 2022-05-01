import cv2
from pathlib import Path
import os

img_files = os.path.join(Path(__file__).parent.absolute(), "img")

first_image_path = os.path.join(img_files, "pic1.jpg")
first_image_name = first_image_path.strip(".jpg").split("/")[-1]

second_image_path = os.path.join(img_files, "pic2.jpg")
second_image_name = first_image_path.strip(".jpg").split("/")[-1]

third_image_path = os.path.join(img_files, "pic3.jpg")
third_image_name = first_image_path.strip(".jpg").split("/")[-1]

if __name__ == "__main__":
    img = cv2.imread(first_image_path)
    cv2.imshow(first_image_name, img)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray", img_gray)

    cv2.waitKey(0)

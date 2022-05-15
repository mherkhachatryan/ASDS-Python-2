import cv2

from pathlib import Path
import os

img_files = os.path.join(Path(__file__).parent.absolute(), "img")

first_image_path = os.path.join(img_files, "pic1.jpg")
first_image_name = first_image_path.strip(".jpg").split("/")[-1]

second_image_path = os.path.join(img_files, "pic2.jpg")
second_image_name = first_image_path.strip(".jpg").split("/")[-1]

if __name__ == "__main__":
    img = cv2.imread(first_image_path)
    cv2.imshow(first_image_name, img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv', hsv)

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    cv2.imshow('lab', lab)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow('rgb', rgb)

    cv2.waitKey(0)
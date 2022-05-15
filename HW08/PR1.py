
import cv2
import os

image_folder = "./img"
file_names = [f"pic{i}.jpg" for i in range(1, 4)]
file_paths = [os.path.join(image_folder, file_names[i]) for i in range(len(file_names))]

if __name__ == "__main__":
    for i in range(len(file_names)):
        img = cv2.imread(file_paths[i])
        cv2.imshow(file_names[i].strip(".jpg"), img)
    cv2.waitKey(0)

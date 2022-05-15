import cv2
import numpy as np

from PR1 import second_image_path, second_image_name


def translate(img, x, y):  # image, # of pixels you want to shift in x and y axes

    trans_mat = np.float32([[1, 0, x], [0, 1, y]])  # translation matrix
    dimensions = (img.shape[1], img.shape[0])  # (width, height)

    return cv2.warpAffine(img, trans_mat, dimensions)


def rotate(img, angle, rot_point=None):  # assume that None - rotating around the center

    (height, width) = (img.shape[0], img.shape[1])

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv2.getRotationMatrix2D(rot_point, angle, 1.0)  # 1.0 - scale
    dimensions = (width, height)

    return cv2.warpAffine(img, rot_mat, dimensions)


if __name__ == "__main__":
    img = cv2.imread(second_image_path)
    cv2.imshow(second_image_name, img)

    translated_image = translate(img, 10, 10)  # image is to small for required parameters image goes out of frame
    cv2.imshow("translated_image", translated_image)

    rotated_translated = rotate(translated_image, angle=50)
    cv2.imshow("rotated_translated", rotated_translated)

    flipped_rotated_translated = flip = cv2.flip(rotated_translated, -1)
    cv2.imshow("flipped_rotated_translated", flipped_rotated_translated)
    cv2.waitKey(0)

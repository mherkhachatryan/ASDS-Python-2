import cv2
from PR1 import file_paths


def rescale_image(frame, scale=0.75, interpolation=cv2.INTER_AREA):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=interpolation)


if __name__ == "__main__":
    img = cv2.imread(file_paths[0])
    img_rescaled = rescale_image(img, scale=0.5)

    cv2.imshow("Original", img)
    cv2.imshow("Rescaled", img_rescaled)

    cv2.waitKey(0)

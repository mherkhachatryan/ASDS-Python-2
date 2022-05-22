import cv2
import matplotlib.pyplot as plt

from PR1 import first_image_path, first_image_name

if __name__ == "__main__":
    img = cv2.imread(first_image_path)
    cv2.imshow(first_image_name, img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # simple thresholding
    threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))
    plt.title('simple thresholding result')
    plt.show()

    # Adaptive mean thresholding

    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 9)

    plt.imshow(cv2.cvtColor(adaptive_thresh, cv2.COLOR_BGR2RGB))
    plt.title('adaptive thresholding result')
    plt.show()
    cv2.waitKey(0)

    # Gaussian Adaptive thresholding
    adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,
                                                     9)

    plt.imshow(cv2.cvtColor(adaptive_thresh_gaussian, cv2.COLOR_BGR2RGB))
    plt.title('gaussian adaptive thresholding result')
    plt.show()

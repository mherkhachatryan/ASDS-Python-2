import cv2
import matplotlib.pyplot as plt

from PR1 import first_image_path, first_image_name

if __name__ == "__main__":
    img = cv2.imread(first_image_path)
    cv2.imshow(first_image_name, img)

    b, g, r = cv2.split(img)

    fig, ax = plt.subplots(3, 1, sharex=True)

    ax[0].hist(b.ravel(), 256, [0, 256], label="b", fc=(0, 0, 1, 0.5))
    ax[1].hist(g.ravel(), 256, [0, 256], label="g", fc=(0, 1, 0, 0.5))
    ax[2].hist(r.ravel(), 256, [0, 256], label="r", fc=(1, 0, 0, 0.5))

    ax[2].set_xlabel("Pixel values")
    for i in range(3):
        ax[i].set_ylabel("log(# of pixels)")
        ax[i].set_yscale("log")  # to make visually interpretable

    plt.show()

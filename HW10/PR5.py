import cv2
import numpy as np

if __name__ == "__main__":
    blank = np.full((400, 400), 128, dtype=np.uint8)

    rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

    circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

    bitwise_xor = cv2.bitwise_xor(circle, rectangle)
    bitwise_or = cv2.bitwise_or(rectangle, circle)
    bitwise_or[bitwise_or == 128] = 0
    bitwise_or[bitwise_or == 255] = 128

    bitwise_xor_3 = bitwise_xor.copy()

    bitwise_xor_3 = np.dstack([bitwise_xor_3, bitwise_xor_3, bitwise_xor_3])
    bitwise_xor_3[:, :, 0][bitwise_xor_3[:, :, 0] == 127] = 155
    bitwise_xor_3[:, :, 1][bitwise_xor_3[:, :, 1] == 127] = 145
    bitwise_xor_3[:, :, 2][bitwise_xor_3[:, :, 2] == 127] = 241

    cv2.imshow("first", bitwise_xor)
    cv2.imshow("second", bitwise_or)
    cv2.imshow("third", bitwise_xor_3)
    cv2.waitKey(0)

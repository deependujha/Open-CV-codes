# resizing
import os

import cv2


img = cv2.imread(os.path.join(".", "bird.jpeg"))

vertical_flip = cv2.flip(img, flipCode=0)
horizontal_flip = cv2.flip(img, flipCode=1)
horizontal_n_vertical_flip = cv2.flip(img, flipCode=-1)


cv2.imshow("img", img)
cv2.imshow("horizontal_flip", horizontal_flip)
cv2.imshow("vertical_flip", vertical_flip)
cv2.imshow("horizontal_n_vertical_flip", horizontal_n_vertical_flip)
cv2.waitKey(0)

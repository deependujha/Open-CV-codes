# crop
import os

import cv2


img = cv2.imread(os.path.join(".", "bird.jpeg"))

print(img.shape)

# image's top-left corner: (0,0)
cropped_img = img[30:150, :]

cv2.imshow("img", img)
cv2.imshow("cropped_img", cropped_img)
cv2.waitKey(0)

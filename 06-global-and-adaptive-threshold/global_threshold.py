import os

import cv2


img = cv2.imread(os.path.join(".", "bear.jpg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# make pixels value below 80 -0, and above that 255
ret, thresh1 = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

thresh2 = cv2.blur(thresh1, (10, 10))
ret, thresh2 = cv2.threshold(thresh2, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.imshow("thresh1", thresh1)
cv2.imshow("thresh2", thresh2)

cv2.waitKey(0)

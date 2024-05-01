import os
import cv2


img = cv2.imread(os.path.join(".", "bird.jpeg"))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


print(f"{img.shape=}")  # img.shape=(183, 275, 3)
print(f"{img_hsv.shape=}")  # img_hsv.shape=(183, 275, 3)
print(f"{img_rgb.shape=}")  # img_rgb.shape=(183, 275, 3)
print(
    f"{img_gray.shape=}"
)  # img_gray.shape=(183, 275) - no 3rd axis, so can't concat with others


# let's concat all these different images and then visualize them
my_concat_img = cv2.hconcat([img, img_rgb, img_hsv])
cv2.imshow("img; gray; rgb; hsv", my_concat_img)
cv2.imshow("img_gray", img_gray)

cv2.waitKey(0)

import os
import cv2


# read image
image_path = os.path.join('.','data', 'bird.jpeg')

img = cv2.imread(image_path)

print(f"{type(img)=}; {img.shape=}")


# write image
cv2.imwrite(os.path.join('.', 'meow', 'bird_out.jpeg'), img)

# visualize image
cv2.imshow('image', img)

# wait for 0 seconds (means until user explicitly closes)
cv2.waitKey(0)

# wait for 5 seconds: `cv2.waitKey(5000)`
# if we don't specify waitKey, opencv will open image and immediately close it.
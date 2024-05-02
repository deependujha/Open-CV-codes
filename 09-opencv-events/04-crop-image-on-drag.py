import cv2
import numpy as np

img = cv2.imread("bird.jpeg")
is_drawing = False
ix = -1  # initial x
iy = -1  # initial y


def draw_on_event(event, x, y, flags, params):
    global img, is_drawing, ix, iy
    # event:
    # - 0: hover
    # - 1: cursor down
    # - 4: cursor up
    if event == 1:
        is_drawing = True
        ix, iy = x, y
    elif event == 4:
        is_drawing = False
        cropped_img = img[iy:y, ix:x]

        print(f"{ix=}; {iy=}; {x=}; {y=}")
        cv2.imshow("cropped_img", cropped_img)
        cv2.waitKey(0)


window_name = "Learning OpenCV Events"

cv2.namedWindow(winname=window_name)

cv2.setMouseCallback(window_name, draw_on_event)


while True:
    cv2.imshow(window_name, img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

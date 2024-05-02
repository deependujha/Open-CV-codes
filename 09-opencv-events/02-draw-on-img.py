import cv2
import numpy as np

img = np.zeros((512, 512, 3))
is_drawing = False


def draw_on_event(event, x, y, flags, params):
    global img, is_drawing
    # event:
    # - 0: hover
    # - 1: cursor down
    # - 4: cursor up
    if event == 0:
        if is_drawing:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == 1:
        is_drawing = True
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    elif event == 4:
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        is_drawing = False


window_name = "Learning OpenCV Events"

cv2.namedWindow(winname=window_name)

cv2.setMouseCallback(window_name, draw_on_event)


while True:
    cv2.imshow(window_name, img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

import cv2
import numpy as np

img = np.zeros((512, 512, 3))


def draw_on_event(event, x, y, flags, params):
    global img
    # event:
    # - 0: hover
    # - 1: cursor down
    # - 4: cursor up
    if event == 0:
        print("mouse moved")
    elif event == 1:
        print("mouse downclick")
    elif event == 4:
        print("mouse upclick")


window_name = "Learning OpenCV Events"

cv2.namedWindow(winname=window_name)

cv2.setMouseCallback(window_name, draw_on_event)


while True:
    cv2.imshow(window_name, img)

    if cv2.waitKey(40) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

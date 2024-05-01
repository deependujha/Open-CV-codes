import cv2

# read webcam

# pass index of the camera that you would like to use.
# Generally, its 0. But, if you have multiple cameras, try 0, 1, 2.., etc.
webcam = cv2.VideoCapture(0) 

# visualize webcam

while True:
    ret, frame = webcam.read()

    cv2.imshow('My WebCam', frame) # create a window with name and frame to display
    
    # wait for 40 milliseconds, before taking another frame. (1000/40 = 25 fps)
    
    # stack overflow question: https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
    if cv2.waitKey(40) & 0xFF == ord('q'): # if user presses on `q`
        break

webcam.release()
cv2.destroyAllWindows()
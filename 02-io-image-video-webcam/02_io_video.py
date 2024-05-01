import os
import cv2


# read video
video_path = os.path.join('.', 'data', 'tom-expression.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True

while ret:
    # ret- return value(true if able to read frame, else false)
    # frame- numpy array (image frame)
    ret, frame = video.read()
    
    if ret:
        cv2.imshow('my image frame window', frame)
        val = cv2.waitKey(40) # wait for 40 millisecond. So, fps = 1000/40 = 25 fps
        

video.release() # release video from memory (RAM)
cv2.destroyAllWindows() # destroy all the windows
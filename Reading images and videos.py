import cv2 as cv  # importing OpenCV

img1 = cv.imread('image.jpg')  # takes in the path of the image and
                               # returns a numpy array with all the pixel values

cv.imshow("Sample Image", img1)  # Takes in "The name of the Window" and the array
                                 # values and displays it in a new window

cv.waitKey(0)  # if the value is 0, then it waits for a key to be pressed,
               # if the value is anything other than 0, say, 12, then it'll wait for 12ms for
               # a key to be pressed (before closing the instance)
               # It returns the code of the pressed key or
               # -1 if no key was pressed before the specified time had elapsed.

cv.destroyAllWindows()  # to close all windows

img2 = cv.imread('large_image.png')
cv.imshow("Large Image", img2)  # You'll notice if you're trying to show a big image, it'll
                                # often get too large and some part of it would get cut out
                                # Don't worry though, we'll solve this issue in the next program
cv.waitKey(0)
cv.destroyAllWindows()

# VIDEO CAPTURE

# To capture a video, we'll use VideoCapture(), that either takes in an integer (like 0, 1, 2,..) or
# the path of the video file. The integers (0, 1, 2, etc) denote the cameras attached to your
# system, so 0 would be the webcam, 1 would be the first camera connected to your system
# 2 would represent the second camera connected to your system and so on...
# We'll basically have to read the video frame-by-frame, and so this is how we do it
# But, in the emd, don't forget to release the Capture


# Video Capture from the Laptop Webcam
capture = cv.VideoCapture(0)
if not capture.isOpened():  # .isOpened() returns true if video capturing has been initialized already
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = capture.read()  # .read() grabs, decodes and returns the next video frame.
                                 # if frame is read correctly ret is True

    cv.imshow('Webcam Feed', frame)  # Display the resulting frame

    # quick reminder, In cv.waitKey(t), if a key is pressed before the particular time t has
    # elapsed, then cv.waitKey() returns the 32-bit integer corresponding to the pressed key
    # AND
    # ord('q') returns Unicode code point of q

    # If q is pressed before the video ends
    if cv.waitKey(1) == ord('q'):  # When the pressed key is q (i.e., when the return value of
                                                                    # waitKey() is equal to the value of q)
        break

    # When the video ends
    if not ret:  # When the video ends and it can't find any more frames to show, ret will return False
        print("Can't receive frame (stream end?). Exiting ...")
        break

# When everything done, release the capture
capture.release()  # .release() closes video file or capturing device
cv.destroyAllWindows()

# PLAYING A VIDEO FILE
cap = cv.VideoCapture('sample_video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

# -215:Assertion failed means that OpenCV could not find a media file at that particular location
# The reason this happened here is because the video ran out of frames. OpenCV couldn't find any frame
# for the last frame of the video and hence gave that error

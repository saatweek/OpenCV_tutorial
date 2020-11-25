import cv2 as cv # importing OpenCV

img1 = cv.imread('image.jpg') # takes in the path of the image and
                              # returns a numpy array with all the pixel values

cv.imshow("Sample Image", img1) # Takes in "The name of the Window" and the array
                                # values and displays it in a new window

cv.waitKey(0) # if the value is 0, then it waits for a key to be pressed,
              # if the value is, say, 1, then it'll wait for 1ms for a key to be
              # pressed(before closing the instance)

cv.destroyAllWindows() # to...well....destroy all windows...? duh

img2 = cv.imread('large_image.png')
cv.imshow("Large Image", img2)
cv.waitKey(0)
cv.destroyAllWindows()

capture = cv.VideoCapture('sample_video.mp4') # We introduce a capture variable here and use the
                                              # function Video Capture. This function can take, either
                                              # integers (0, 1, 2..) where 0 is your webcam, 1 is
                                              # your 1st camera, 2 is your 2nd camera and so on... OR,
                                              # it can take the path of your video file

# Now we'll basically have to read the video frame-by-frame, and so this is how we do it

while True:
    isTrue, frame = capture.read() # capture.read returns two variables, a frame and a boolean
                                   # that tells wheather the frame was successfully read or not

    cv.imshow("Video", frame)  # displaying the frame in a window

    if cv.waitKey(20) & 0xFF == ord('f'): # and then waitKey(20) means that it'll wait for
                                          # 20ms before showing another frame and the 0xFF == ord('f')
                                          # will close the window whenever the f key is pressed
        break

capture.release() # release the capture device
cv.destroyAllWindows() # destroy all windows

# -215:Assertion failed means that OpenCV could not find a media file at that particular location
# The reason this happened here is because the video ran out of frames. OpenCV couldn't find any frame
# for the last frame of the video and hence gave that error
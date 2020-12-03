import cv2 as cv

#Reading and Rescaling Images
img = cv.imread('large_image.png')  #reading the large image
cv.imshow('Large Image', img)  # showing the image
cv.waitKey(0)  # waiting for a key to be pressed (before showing the next image)
scale = 0.2  # deciding how much we want to shrink it by

# .resized() takes in 3 arguments and returns another numpy array with the pixel values
# img.shape[0] would be the height of the image, and img.shape[1] would be the width of the
# image.
# The dimensions of the image are in a tuple of (width, height)
# We multiply the width and height by the scale and take the integer value of it
img_resized = cv.resize(img,  # the original image you want to modify
                        (int(img.shape[1] * scale), int(img.shape[0] * scale)),  # dimensions
                        interpolation=cv.INTER_AREA)
# Interpolation is used when you modify the size of the image.
# cv.INTER_NEAREST is the fastest, but also gives worst results
# cv.INTER_AREA is a good algorithm to use when you decrease the size of the image
# cv.INTER_LINEAR is used when you increase the size of the image
# cv.INTER_CUBIC is also used when increasing the size of the image. It yields better
# results than linear, but is also slower

cv.imshow("Large Image Resized", img_resized)
cv.waitKey(0)
cv.destroyAllWindows()


# Resizing Videos
# This is almost exactly equal to resizing images, except you do this to each frame
capture = cv.VideoCapture("sample_video.mp4")
while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        print("Can't receive frame (Stream end?). Exiting..")
        break

    resized_frame = cv.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale)), interpolation=cv.INTER_AREA)
    cv.imshow("Video", frame)
    cv.imshow("Resized Video", resized_frame)


    if cv.waitKey(24) == ord('q'):
        break
capture.release()
cv.destroyAllWindows()




def changeRes(width, height): # Only works for live video
    capture.set(16, width)
    capture.set(9, height)

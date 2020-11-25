import cv2 as cv

def rescaleFrame(frame, scale=0.75): # Works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # Returns a resized frame

#Reading and Rescaling Images
img = cv.imread('large_image.png')
cv.imshow('Large Image', img)
cv.waitKey(0)
img_resized = rescaleFrame(img, 0.1)
cv.imshow("Large Image Resized", img_resized)
cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture("sample_video.mp4")

while (True):
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.50)

    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('f'):
        break

capture.release()
cv.destroyAllWindows()

def changeRes(width, height): # Only works for live video
    capture.set(16, width)
    capture.set(9, height)

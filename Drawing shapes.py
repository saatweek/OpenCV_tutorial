import cv2 as cv
import numpy as np

# Making a Blank black Image of size (500, 500, 3).
# Since all the pixel values would be zero
blank = np.zeros((300, 300, 3), dtype='uint8')
cv.imshow("Blank Image", blank)

# If we change the third channel to 0, 255 and, 0, we'll get a Green Image according to BGR
blank[:] = 0, 255, 0
cv.imshow("Green", blank)

# Important Note regarding the co-ordinates of an image
# The origin of an image is considered to be in the top left corner of the image
# The positive x-axis lies to it's right and the +ve y-axis lies to it's bottom

# Drawing a Rectangle
blank = np.zeros((300, 300, 3), dtype='uint8')
cv.rectangle(blank,  # the target image over which the rectangle would be drawn
             (0, 0),  # the origin of rectangle
             (150, 300),  # size of (Breadth, length)
             (0, 0, 255),  # Colour of the rectangle
             thickness=1)  # Thickness of the rectangle, specify -1 to fill the rectangle
cv.imshow("Rectangle", blank)

blank2 = np.zeros((300, 300, 3), dtype="uint8")
cv.rectangle(blank2, (0, 0), (blank2.shape[1]//3, blank2.shape[0]//3), (255, 0, 0), thickness=-1)
cv.imshow("Alternative Rectangle (Filled)", blank2)

# Drawing a Circle
cv.circle(blank, # target image over which to draw the circle
          (blank.shape[1]//2, blank.shape[0]//2),  # centre of the circle
          50,  # radius of the circle
          (0, 255, 0),  # colour of the circle
          1)  # the thickness of the circle, set to -1 to fill the circle
cv.imshow("circle", blank)

# Drawing a line
cv.line(blank2,  # target image over which we want to draw the line
        (blank2.shape[1]//3, 2*blank2.shape[0]//3),  # starting point of the line
        (2*blank2.shape[1]//3, blank2.shape[0]//3),  # ending point of the line
        (0, 255, 0),  # colour of the line
        thickness=1)  # thickness of the line
cv.imshow("Line", blank2)

# Writing Text Over an Image
cv.putText(blank,  # target image over which to write
           "Hello World!",  # text to be written
           org=(10, 250),  # origin of the text (where the text starts from)
           fontFace=cv.FONT_HERSHEY_SIMPLEX,  # font of the text
           fontScale=1.0,  #thickness of the text
           color=(255, 0, 0))  # colour of the text
cv.imshow("Text", blank)

cv.waitKey(0)
cv.destroyAllWindows()

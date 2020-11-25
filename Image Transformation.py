import cv2 as cv
import numpy as np

# Resize an image in one line
img = cv.imread("large_image.png")
img_resized = cv.resize(img,
                        (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)),
                        interpolation=cv.INTER_AREA)
cv.imshow("Image", img_resized)

# Translation : refers to the shifting of an image
def translate(img, x, y): #x and x refer to the number of pixels
                          # you want to shift in the respective direction
                          # -x --> Left
                          # -y --> Up
                          # x --> Right
                          # y --> Down
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # takes in a list with 2 lists inside of it
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img_resized, 100, 100)
cv.imshow("translated Image", translated)

#Rotation
def rotate(img,              # Image to be rotated
           angle,            # angle to rotate around
           rotPoint = None): # rotation point
    (height, width) = img.shape[:2] # grabbing the height and the width of the image by
                                    # taking the first two values of img.shape

    if rotPoint is None: #if the rotation point is None, we'll rotate around the centre
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, # a point to rotate around
                                    angle, # degrees of rotation
                                    1.0) #scale value
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img_resized, 45) #this will rotate the image anti-clockwise
cv.imshow("Rotated", rotated)
# If you rotate an already rotated image, then the black spaces in the
# original rotated images will be included in the new one

# Flipping
flip = cv.flip(img_resized,
               1) # This can either be 0, 1, or -1
                  # 0 --> vertical flip
                  # 1 --> horizontal flip
                  # -1 --> both vertical and horizontal flip
cv.imshow("Flipped Image", flip)

# Cropping an Image (basically we use array slicing)
cropped = img_resized[200:400, 300:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)
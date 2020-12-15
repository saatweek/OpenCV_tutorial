import cv2 as cv
import numpy as np

# Resize an image in one line
img = cv.imread("large_image.png")
img = cv.resize(img,  # original image to be resized
               (int(img.shape[1] * 0.15), int(img.shape[0] * 0.15)), # dimensions of the final resized image
               interpolation=cv.INTER_AREA)


# What is an Affine Transformation?
#
# 1. A transformation that can be expressed in the form of a matrix multiplication (linear transformation)
#    followed by a vector addition (translation)
# 2. From the above, we can use an Affine Transformation to express:
#    a) Rotations (linear transformation)
#    b) Translations (vector addition)
#    c) Scale operations (linear transformation)

# We'll use the cv.warpAffine() function to achieve all three of these
# This function takes in 3  parameters :
# 1. Original image to be translated
# 2. Matrix for the linear transformation of the image
# 3. Dimensions of the output image

# Translation : refers to the shifting of an image
# (Remember,  the origin of an image is at the top left corner)
# The +ve x axis is to the right and the +ve y-axis is towards the bottom

# The matrix required for the translation of an image is in the form of
# [[1  0  x]
#  [0  1  y]]

# x and y refer to the number of pixels you want to shift in the respective direction
# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down

transMat = np.float32([[1, 0, 100],
                       [0, 1, 100]])       # Translation Matrix has to be in float32
dimensions = (img.shape[1], img.shape[0])  # specifying the shape of the output image

translated = cv.warpAffine(img, transMat, dimensions)
cv.imshow("translated Image", translated)

# Rotation

# Since the matrix required for the image rotation is a bit complex, we'll use the in-built function in OpenCV called
# cv.getRotationMatrix2D() which takes in 3 parameters :
# 1. center	: Center of the rotation in the source image.
# 2. angle	: Rotation angle in degrees. Positive values mean counter-clockwise rotation
#             (the coordinate origin is assumed to be the top-left corner).
# 3. scale	: Isotropic scale factor.

rotated = cv.warpAffine(img,  # original image to be rotated
                        cv.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2),  # centre of rotation
                                               45, # degree of rotation
                                               1), # scale
                        (img.shape[1], img.shape[0]) # dimensions of the final image
                        )
cv.imshow("Rotated", rotated)

# If you rotate an already rotated image, then the black spaces in the
# original rotated images will be included in the new one

# If you don't want the image to cut when using cv.warpAffine(), then lower the dimensions of the final image

# Flipping
flip = cv.flip(img,
               1)  # This can either be 0, 1, or -1
                   #  0 --> vertical flip
                   #  1 --> horizontal flip
                   # -1 --> both vertical and horizontal flip
cv.imshow("Flipped Image", flip)

# Cropping an Image (basically we use array slicing)
cropped = img[100:8000, 100:4000]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)
cv.destroyAllWindows()
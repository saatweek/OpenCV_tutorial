import cv2 as cv
import numpy as np

# Resizing the large image
img = cv.imread("large_image.png")
scale=0.1
resized_img = cv.resize(img, (int(img.shape[1] * scale), int(img.shape[0]*scale)),
                        interpolation=cv.INTER_AREA)
cv.imshow("large Image Resized", resized_img)


# Converting to grayscale
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow("Resized Gray Image", gray)

# Blurring the image
# Gaussian Blur basically takes a window frame and passes it throughout the image taking a gaussian weighted average
# over the middle point of the (part of the)image under the filter (that's why we can only take odd number)
# There are other types of blurs as well, but Gaussian is the most preferred.
blur = cv.GaussianBlur(resized_img,
                       (17, 17),          # This must be some odd number
                       cv.BORDER_DEFAULT) # This decides the border type. Let this be average
cv.imshow("Blurred Image",blur)


# Edge Cascade : Will show the edges
mean_val = np.mean(gray)      # finding the mean pixel intensity of the entire grey image
min_thres = 0.66 * mean_val   # minimum threshold is the minimum intensity of pixel, under which we're sure that the pixel doesn't belong to a boundary
                              # ideal value = 0.66 * mean pixel intensity of b&w image
max_thres = 1.33 * mean_val   # Maximum threshold is the maximum intensity of pixel, over which we're sure that the pixel is a part of an edge
                              # ideal value = 1.33 * mean pixel intensity of b&w image
canny = cv.Canny(resized_img,            # source image
                 min_thres, max_thres)   # Second and third arguments are our min Threshold Value and max threshold Value respectively.
cv.imshow("Canny Edges", canny)
# If you want to reduce the number of edges, then blur the image and then pass it through the canny cascade

# Dilation and erosion are two fundamental morphological operations.
# Dilation adds pixels to the boundaries of objects in an image, while erosion removes pixels on object boundaries

# DILATION                                                             | EROSION
# _____________________________________________________________________|_______________________________________________________________
# 1. It increases the size of the objects.	                           | 1. It decreases the size of the objects.
# 2. It fills the holes and broken areas.	                           | 2. It removes the small anomalies.
# 3. It connects the areas that are separated by space smaller         | 3. It reduces the brightness of the bright
#    than structuring element.                                         |    objects.
# 4. It increases the brightness of the objects.	                   | 4. It removes the objects smaller than the structuring element.

# Dilating the Image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilated Image", dilated)

# Eroding : You'll get back the same edge cascade if that window size and iterations are the same
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroded", eroded)


# Cropping
cropped = img[50:100, 200:400] #Just select the pixel range to show
cv.imshow("Cropped", cropped)

cv.waitKey(0)
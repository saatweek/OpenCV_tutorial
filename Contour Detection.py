import cv2 as cv
import numpy as np

# Loading, Rescaling and Showing the main image
img = cv.imread("large_image.png")
img = cv.resize(img, (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)), interpolation=cv.INTER_AREA)
cv.imshow("Image", img)

# Ok, What are Contours and How are they different from edges?

# Edges are computed as points that are extrema of the image gradient in
# the direction of the gradient
#
# Contours are often obtained from edges, but they are aimed at being object contours.
# Thus, they need to be closed curves. We can think of them as
# boundaries. When they are obtained from edges, you need to connect the
# edges in order to obtain a closed contour.

# Converting the image to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image", gray)

mean_val = np.mean(gray)
min_val = 0.66 * mean_val
max_val = 1.33 * mean_val

# Grabbing the edges in the picture
canny = cv.Canny(gray, min_val, max_val) 
cv.imshow("Canny Edges", canny)

#_______________________IMPORTANT STUFF_____________________________#

# FINDING CONTOURS

# cv.findContours() finds contours in a binary image
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# OK. Lots of new terms used. Let's explain the use of each one of them.

# Contours can be explained simply as a curve joining all the continuous
# points (along the boundary), having same color or intensity.
# That's why they're used for object detection and are obtained from edges
# cv.findContours returns 2 things :
#                                   1. Contours : Detected contours. Each contour is stored as a
#                                                 vector of points (a list)
#                                   2. Hierarchy: Hierarchy shows how different contours are
#                                                 linked to each other (if some contour is within
#                                                 some other contour or if it contains other contours)
#                                                 It has as many elements as the number of
#                                                 contours. It's an optional output vector
#
# It accepts the following parameters :
#                                   1. image    : Source image of which you'll find the contours.
#                                                 You can use compare, inRange, threshold ,
#                                                 adaptiveThreshold, Canny, and others to create
#                                                 a binary image out of a grayscale or color one.
#                                   2. Mode     : How the contours are obtained. 3 main types
#
# |---------------------------------------------------------------------------------|
# | cv.RETR_EXTERNAL       | retrieves only the extreme outer contours.             |
# |________________________|________________________________________________________|
# | cv.RETR_LIST           | retrieves all of the contours without establishing any |
# |                        | hierarchical relationships.                            |
# |________________________|________________________________________________________|
# | cv.RETR_TREE           | retrieves all of the contours and reconstructs a full  |
# |                        | hierarchy of nested contours.                          |
# |------------------------|--------------------------------------------------------|
#
#                                  3. Method    : Contour approximation method. 2 main types
#
# |------------------------|--------------------------------------------------------|
# | cv.CHAIN_APPROX_NONE   | stores absolutely all the contour points.              |
# |_______________________ |________________________________________________________|
# | cv.CHAIN_APPROX_SIMPLE | compresses horizontal, vertical, and diagonal segments |
# |                        | and leaves only their end points. For example, an      |
# |                        | up-right rectangular contour is encoded with 4 points. |
# |------------------------|--------------------------------------------------------|


print(f'{len(contours)} contour(s) found in original b&w image using Canny Edges')

# If you're using the same image as mine, you'll notice that the there are 1084 contours found...
# which is, kind of, a lot. Let's blur the b&w image and then find the contours again
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)
canny2 = cv.Canny(blur, min_val, max_val) 
cv.imshow("Canny Edges",canny2)
contours2, hierarchies2 = cv.findContours(canny2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} contour(s) found after blurring the b&w image and using Canny Edges')


# Now let's find the contours using a Threshold
# It return 2 values retval and thresholded Image (We'll explain the use of retval later)
ret, thresh = cv.threshold(gray,  # source image (IT SHOULD BE A GREYSCALE IMAGE)
                           30,    # minimum value below which everything will be blacked out
                                  # changing this value gives wildly different pictures
                           255,   # max value to which the values (above min values) will be increased
                           cv.THRESH_BINARY)  # Type of threshold we want
                                              # There's also cv.THRESH_BINARY_INV which just inverts
                                              # the results (the black would be white and vice-versa)
cv.imshow("Threshold", thresh)

contours3, hierarchies3 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours3)} contour(s) found after regular threshold of the b&w image')

# Drawing the Contours found from Binary threshold image
blank_image = np.zeros(img.shape, dtype='uint8')  # blank image
cv.drawContours(blank_image,  # image to draw over
                contours3,    # takes in a list of contours (which is already a list)
                -1,           # contours index, to decide how many contours you want to show
                              # We want to show all of them, hence, -1
                (255, 0, 0),  # setting the colour of contours (b,g,r)
                1)            # Thickness
cv.imshow("Contours by thresholding", blank_image)

# Did you notice how wildly the images differed when we changed the threshold value?
# So, how can we know if the selected threshold value is ideal or not?
# Answer is, trial and error method. But consider a bimodal image
# (In simple words, bimodal image is an image whose histogram has two peaks).
# For that image, we can approximately take a value in the middle of those peaks as threshold
# value, right ? That is what Otsu binarization does.
# So in simple words, it automatically calculates a threshold value from image histogram
# for a bimodal image. (For images which are not bimodal, binarization won’t be accurate.)
# For threshold value, simply pass zero.
# Then the algorithm finds the optimal threshold value and returns you as the second output, retVal.
# If Otsu thresholding is not used, retVal is same as the threshold value you used.

ret2, thresh2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Otsu Threshold greyscale image", thresh2)
contours4, hierarchies4 = cv.findContours(thresh2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours4)} contour(s) found after Otsu thresholding of the b&w image')

ret3, thresh3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow("Otsu Threshold on Blurred Image", thresh3)
contours5, hierarchies5 = cv.findContours(thresh3, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours5)} contour(s) found after Otsu thresholding the blurred b&w image')

# Trying Out Adaptive Thresholding
# In this, the algorithm calculate the threshold for a small regions of the image.
# So we get different thresholds for different regions of the same image and it gives us
# better results for images with varying illumination.
thresh4 = cv.adaptiveThreshold(gray, 255,
                               cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # Threshold value is the
                                                               # weighted sum of neighbourhood values
                                                               # where weights are a gaussian window.
                                                               # There's also cv2.ADAPTIVE_THRESH_MEAN_C
                                                               # where threshold value is the mean of
                                                               # neighbourhood area.
                               cv.THRESH_BINARY, 11, 2)
cv.imshow("Adaptive Threshold", thresh4)
contours6, hierarchies6 = cv.findContours(thresh4, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours6)} contour(s) found after dynamically thresholding the b&w image')


# OK, now for

cv.waitKey(0)
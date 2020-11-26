import cv2 as cv
import numpy as np

#Function to rescale
def rescaleFrame(frame, scale = 0.2):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Resizing the large image
img = cv.imread("large_image.png")
resized_img = rescaleFrame(img)
cv.imshow("large Image Resized", resized_img)


# Converting to grayscale
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow("Resized Gray Image", gray)

# Blurring the image
# Gaussian Blur basically takes a window frame and passes it throughout the image
# taking a gaussian weighted average over the middle point of the
# (part of the)image under the filter
# (that's why we can only take odd number)
# There are other types of blurs as well, but Gaussian is the most preferred
blur = cv.GaussianBlur(resized_img,
                       (17, 17),          # This must be some odd number
                       cv.BORDER_DEFAULT) # This decides the border type. Let this be average
cv.imshow("Blurred Image",blur)


# Edge Cascade : Will show the edges
mean_val = np.mean(gray)      # finding the mean pixel intensity of the entire grey image
min_thres = 0.66 * mean_val   # minimum threshold is the minimum intensity of pixel, under
                              # which we're sure that the pixel doesn't belong to a boundary
                              # ideal value = 0.66 * mean pixel intensity of b&w image
max_thres = 1.33 * mean_val   # Maximum threshold is the maximum intensity of pixel, over which
                              # we're sure that the pixel is a part of an edge
                              # ideal value = 1.33 * mean pixel intensity of b&w image
canny = cv.Canny(resized_img,            # source image
                 min_thres, max_thres)   # Second and third arguments are our min Threshold Value
                                         # and max threshold Value respectively.
cv.imshow("Canny Edges", canny)
# If you want to reduce the number of edges, then blur the image and then pass
# it through the canny cascade

# Dilating the Image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilated Image", dilated)

# Eroding : You'll get back the same edge cascade if that window size and iterations are the same
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroded", eroded)

# Resizing Image : ignores the aspect ratio
resized = cv.resize(resized_img, # takes the image to be resized
                    (500, 500),  # Final pixel counts
                    interpolation=cv.INTER_AREA) # cv.INTER_AREA is good if
                                                 # you're downsizing the image
                    # If you're increasing the size of the image, then cv.INTER_LINEAR
                    # or cv.INTER_CUBIC. cv.INTER_CUBIC is the slowest among them all, but the
                    # resulting quality of the image is often, much higher
cv.imshow("Resized", resized)

# Btw,this cv.resize is the same function we used in the rescaleFrame() function
# If we want to mimic the effect of rescaleFrame() directly from here, then we'll write..
img_resized = cv.resize(img,
                        (int(img.shape[1] * 0.2), int(img.shape[0] * 0.2)),
                        interpolation=cv.INTER_AREA)
cv.imshow("resized Image directly", img_resized)


# Cropping
cropped = img[50:100, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
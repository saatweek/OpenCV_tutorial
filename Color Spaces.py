import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

scale = 0.1
img = cv.imread("large_image.png")
img = cv.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)), interpolation=cv.INTER_AREA)
cv.imshow("Original Image", img)
# The default way of reading images in OpenCV is in BGR

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("b&w Image", gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB Image", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB Image", rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV to BGR", hsv_bgr)

cv.waitKey(0)
cv.destroyAllWindows()

# Now we'll split the Image in their corresponding blue, green and red components
cv.imshow("Original Image", img)
b, g, r = cv.split(img) # This gives us 3 numpy arrays that have the intensities
                        # of Blue, Green and Red respectively
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

cv.waitKey(0)
cv.destroyAllWindows()
# You'll see that all of these images are actually in b&w. And it's fair since their respective
# numpy arrays only contain the intensity values of their own individual colour


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Let's try and visualize these intensity matrices in their own respective colours

# making a blank black picure
blank = np.zeros(img.shape[:2], dtype="uint8")

cv.imshow("Original Image", img)
blue = cv.merge([b, blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("Blue Image", blue)
cv.imshow("Green Image", green)
cv.imshow("Red Image", red)


cv.waitKey(0)
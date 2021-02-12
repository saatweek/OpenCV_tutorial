import cv2 as cv

img = cv.imread('IMG_20201209_122824.jpg')  # selfie
img = cv.resize(img, (int(img.shape[1]*0.1), int(img.shape[0]*0.1)), interpolation=cv.INTER_AREA)  # resizing
cv.imshow("Face Image", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #converting the selfie to grey scale
cv.imshow("B&W Image", grey)

# To use a Haar Cascade, you'll first have to download its XML file. It can be found in https://github.com/saatweek/OpenCV_tutorial
# The CascadeClassifier takes in the path of the classifier. Since I have it in the same folder as this Python file. I'll simply 
# write the file name. 
# We make a cascade classifier object and pass in the appopriate parameter.
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# detect Multiscale returns the bounding rectangles for the detected faces
faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)
print("No. of faces found = ", len(faces_rect))

# Drawing the found rectangles over the original image
for (x, y, w, h) in faces_rect:
    cv.rectangle(grey, (x, y), (x+w, y+h), (0, 0, 255), thickness=1)

cv.imshow("Detected Face", grey)

# Same for the group image
group_img = cv.imread('group.jpg')
group_img = cv.resize(group_img, (int(group_img.shape[1]*0.8), int(group_img.shape[0]*0.8)), interpolation=cv.INTER_AREA)

faces_rect = haar_cascade.detectMultiScale(group_img, scaleFactor=1.1, minNeighbors=8)
print("No. of Faces Detected = ", len(faces_rect))

for (x, y, w, h) in faces_rect:
    cv.rectangle(group_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Group Image", group_img)

cv.waitKey(0)
cv.destroyAllWindows()

capture = cv.VideoCapture(0)
while capture.isOpened():
    isTrue, frame = capture.read()

    if not isTrue:
        print("Can't receive frame (stream end..?). Exiting")
        break
    # using a b&w image sometimes helps with better recognition, we'll just comment it out for now
    # bwframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=30)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv.imshow("Video Capture", frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()


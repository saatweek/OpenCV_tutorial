# First, we download mtcnn using the command `pip install mtcnn`.
# We can then check the installation using `pip show mtcnn`

from mtcnn import MTCNN
import cv2 as cv
img = cv.imread('group.jpg')  # reading the image
img_resized = cv.resize(img, (int(img.shape[1]*0.5), int(img.shape[0]*0.5)), interpolation=cv.INTER_AREA)  # resizing

converted_img = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)
# initializing a MTCNN object
detector = MTCNN()
result = detector.detect_faces(converted_img)
# the detect_faces function return a list of json objects. Here for example, it is :
'''
[{'box': [203, 133, 48, 57], 
  'confidence': 0.9999998807907104, 
  'keypoints': {'left_eye': (217, 155), 
                'right_eye': (239, 154), 
                'nose': (229, 164), 
                'mouth_left': (218, 174), 
                'mouth_right': (241, 173)}}, 
 {'box': [446, 83, 46, 54], 
  'confidence': 0.9999861717224121, 
  'keypoints': {'left_eye': (458, 102), 
                'right_eye': (479, 99), 
                'nose': (469, 112), 
                'mouth_left': (461, 122), 
                'mouth_right': (482, 119)}}, 
 {'box': [344, 106, 41, 48], 
  'confidence': 0.9999454021453857, 
  'keypoints': {'left_eye': (356, 122), 
                'right_eye': (375, 120), 
                'nose': (365, 133), 
                'mouth_left': (357, 140), 
                'mouth_right': (376, 139)}}, 
 {'box': [197, 382, 29, 35], 
  'confidence': 0.7023869752883911, 
  'keypoints': {'left_eye': (206, 397), 
                'right_eye': (218, 394), 
                'nose': (213, 403), 
                'mouth_left': (210, 411), 
                'mouth_right': (220, 408)}}]
'''
print(result)

# So for each json object in the list, we make a rectangle with the given dimensions
for faces in result:
    print(faces)
    bounding_box = faces['box']
    keypoints = faces['keypoints']
    cv.rectangle(img_resized, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (0, 255, 0), thickness=2)
    cv.circle(img_resized, keypoints['left_eye'], 1, (0, 0, 255), 1)
    cv.circle(img_resized, keypoints['right_eye'], 1, (0, 0, 255), 1)

cv.imshow('Detected Faces', img_resized)
cv.waitKey(0)
cv.destroyAllWindows()

# Let us now try and identify people from a live video feed
capture = cv.VideoCapture(0)
while capture.isOpened():
    isTrue, frame = capture.read()

    if not isTrue:
        print("Can't receive frame (stream end..?). Exiting")
        break
    faces = detector.detect_faces(frame)
    for face in faces:
        bounding_box = face['box']
        cv.rectangle(frame, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (255, 0, 0), thickness=1)
    cv.imshow("Video Capture", frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
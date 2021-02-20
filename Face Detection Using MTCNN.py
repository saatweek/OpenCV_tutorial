from mtcnn import MTCNN
import cv2 as cv
img = cv.imread('group.jpg')
img_resized = cv.resize(img, (int(img.shape[1]*0.5), int(img.shape[0]*0.5)), interpolation=cv.INTER_AREA)

converted_img = cv.cvtColor(img_resized, cv.COLOR_BGR2RGB)
detector = MTCNN()
result = detector.detect_faces(converted_img)
print(result)
for faces in result:
    print(faces)
    bounding_box = faces['box']
    cv.rectangle(img_resized, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (0, 255, 0), thickness=2)


cv.imshow('Detected Faces', img_resized)
cv.waitKey(0)
cv.destroyAllWindows()




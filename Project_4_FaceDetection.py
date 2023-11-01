import cv2

img=cv2.imread('Images/img.png')
cv2.imshow('Person',img)
img_group=cv2.imread("Images/img_2.png")


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_group=cv2.cvtColor(img_group,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.imshow("gray group",gray_group)

haar_cascade=cv2.CascadeClassifier('haar_face.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
faces_rect_group=haar_cascade.detectMultiScale(gray_group,scaleFactor=1.1,minNeighbors=4)

print(f'number of faces found ={len(faces_rect)}')
print(f'number of faces found in group ={len(faces_rect_group)}')

for(x,y,w,h) in faces_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
for (x, y, w, h) in faces_rect_group:
    cv2.rectangle(img_group, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

cv2.imshow('Detected Faces',img)
cv2.imshow('Detected group Faces',img_group)






cv2.waitKey(0)
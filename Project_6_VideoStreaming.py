import cv2
import numpy as np


video=cv2.VideoCapture(0)


grayscale_flag=0
hsv_flag=0
while True:
    Success,frame=video.read()
    key = cv2.waitKey(1) & 0xFF
    cv2.imshow("Original Camera", frame)
  
    

    if key == ord('S'):
        cv2.imwrite("captured_frame.jpg", frame)
        print("Frame saved as captured_frame.jpg")

    

    if key == ord('G'):
        grayscale_flag = not grayscale_flag
        if grayscale_flag:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    if key == ord('H'):
        hsv_flag = not hsv_flag
        if hsv_flag:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



  


    if key == ord('O'):
        cv2.imshow("Original Frame", frame)



    if key ==ord('q'):
        break

video.release()
cv2.destroyAllWindows()

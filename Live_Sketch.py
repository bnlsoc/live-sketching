import cv2
import numpy as np
def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #Gaussian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0) #grayscale_image,kernel_size,variance
    return cv2.divide(img_gray,img_gray_blur+2, scale=256)
cap = cv2.VideoCapture(0) #0 for instantaneous video capture
while True:
    ret,frame = cap.read()
    x = sketch(frame)
    cv2.imshow('Your Live Sketch',x)
    cv2.imwrite('./yoursketch.jpg',x)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

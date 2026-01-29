import cv2
#import numpy as np

image = cv2.imread("sanjay.jpg")

if image is None:
    print("opps! image not found")

else:
    resized_image = cv2.resize(image,(500,800))
    kernel = 3  #only odd number hunxa kinaki center valuebata transfere hunxa like 3*3 matrix hunxa tesma center value hunxa 
    blurred_image = cv2.medianBlur(resized_image,kernel)
    cv2.imshow("original image",resized_image)
    cv2.imshow("blurred image",blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
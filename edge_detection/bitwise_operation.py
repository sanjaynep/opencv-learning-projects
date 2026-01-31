import cv2
import numpy as np

#height and width has to be same
img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

rectangle = cv2.rectangle(img1,(50,50),(150,150),255,-1)
circle = cv2.circle(img2,(150,150),100,255,-1)

bitwise_and = cv2.bitwise_and(rectangle,circle)
bitwise_or = cv2.bitwise_or(rectangle,circle)
bitwise_not = cv2.bitwise_not(circle)

cv2.imshow("rectangle",rectangle)
cv2.imshow("circle",circle)
cv2.imshow("and",bitwise_and)
cv2.imshow("or",bitwise_or)
cv2.imshow("not",bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
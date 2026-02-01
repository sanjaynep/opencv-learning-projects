import cv2
import numpy as np

image = np.zeros((1000,1000,3), dtype= np.uint8)

points = np.array([[500,100],
                   [400,300],
                   [600,300]
                   ],np.int32)
# in every drawing for quadrilator,polygons or many more
points = points.reshape((-1,1,2))
cv2.fillPoly(image,[points],(0,0,255))

#circle ko lagi
# cv2.circle(image, center=(500,500), radius=200, color=(0,0,255), thickness=-1)


#yo garna pardaina if channel value pass nagare ano color 200 vaye
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
#cv2.imshow("gray",gray_image)

ret,threshold_image = cv2.threshold(gray_image,50,255,cv2.THRESH_BINARY)
#cv2.imshow("thrrsimage",threshold_image)

contours,hierarcy = cv2.findContours(threshold_image,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_SIMPLE)
print(f"the number of contours:{len(contours)}")
cv2.drawContours(image,contours=contours,contourIdx=-1,color=(0,255,0),thickness=1)


for contour in contours:
    # approx(contour.epsilon)
    conter = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    sides = len(conter)
    if sides == 1:
        print("line")
        shape_name = "line"
    elif sides == 2:
        print("double line")
        shape_name = "Two sides line"
    elif sides == 3:
        print("triangle")
        shape_name = "triangle"

    elif sides == 4:
        print("quadrilateral")
        shape_name = "quadrilateral"

    elif sides == 5:
        print("polygon")
        shape_name = "pentagon"

    elif sides > 5:
        shape_name = "circle"

    else:
        print("circle")
        shape_name = "unknown"

    cv2.drawContours(image,contours=[conter],contourIdx=-1,color=(0,255,0),thickness=1)
    x = conter.ravel()[0] - 10
    y = conter.ravel()[1] 

    cv2.putText(image,shape_name,(x,y),1,cv2.FONT_HERSHEY_COMPLEX ,(0,255,0),2)
cv2.imwrite("shape.png",image)
cv2.imshow("detected image",image)         
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

image = cv2.imread("sanjay.jpg")

if image is None:
    print("image not found")

else:
    resized_image = cv2.resize(image,(500,500))
    p1 = (100,400)
    p2 = (400,100)
    color = (125,245,154)
    cv2.rectangle(resized_image,p1,p2,color,3)
    cv2.imshow("sanjay",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2

image  = cv2.imread("sanjay.jpg")

if image is None:
    print("image not found")

else:
    resized_image = cv2.resize(image,(600,500))
    cv2.circle(resized_image,(240,190),80,(0,255,0),2)
    cv2.imshow("sanjay",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


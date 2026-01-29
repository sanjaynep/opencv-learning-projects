import cv2

image  = cv2.imread("sanjay.jpg")

if image is None:
    print("image not found")

else:
    resized_image = cv2.resize(image,(600,500))
    # for text
    cv2.putText(resized_image,"hello sanjay",(50,400),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1.5,(100,0,0),1)
    cv2.imshow("sanjay",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



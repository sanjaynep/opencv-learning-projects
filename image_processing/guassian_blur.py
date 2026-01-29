import cv2

image = cv2.imread("sanjay.jpg")

if image is None:
    print("opps! image not found")

else:
    resized_image = cv2.resize(image,(500,800))
    # kernel value jaile odd ma hunxa
    blurred_image = cv2.GaussianBlur(resized_image,(3,3),0)
    cv2.imshow("original image",resized_image)
    cv2.imshow("blurred image",blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2

image =  cv2.imread("sanjay.jpg",cv2.IMREAD_GRAYSCALE)
if image is None:
    print('opps image not found')
else:
    resized_image = cv2.resize(image,(500,800))
    retval, thresold_image = cv2.threshold(resized_image,120,255,cv2.THRESH_BINARY)
    cv2.imshow("original image",resized_image)
    cv2.imshow("threshold image",thresold_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



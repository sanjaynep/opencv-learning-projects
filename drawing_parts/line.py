import cv2

image =cv2.imread("sanjay.jpg")

if image is None:
    print("oops! image not found")
else:

    resized_image=cv2.resize(image,(500,500))
    l1 = (100,200)
    l2 = (300,200)
    color = (0,255,0)
    cv2.line(resized_image,l1,l2,color,1)
    cv2.imshow("sanjay",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



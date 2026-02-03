import cv2

image = cv2.imread("sanjay.jpg",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("opps! image not found")

else:
    resized_image =  cv2.resize(image,(500,800))
    canny_image =  cv2.Canny(resized_image,50,150)
    cv2.imshow("contrasted image",canny_image)
    cv2.imshow("original image",resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
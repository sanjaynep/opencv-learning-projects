import cv2

image=cv2.imread("sanjay.jpg")
if image is None:
    print("error")
else:
    resized=cv2.resize(image,(500,500))
    height,width = resized.shape[:2]
    center=(height//2,width//2)
    rotation=cv2.getRotationMatrix2D(center,360,2.0)
    rotated_image = cv2.warpAffine(resized,rotation,(500,500))
    flipped_horizontal_image=cv2.flip(resized,0)
    flipped_vertical_image=cv2.flip(resized,1)
    flipped_both_image=cv2.flip(resized,-1)
   # cv2.imshow("first_image",resized)
    #cv2.imshow("rotated_image",rotated_image)
    cv2.imshow("flipped_horizontal_image",flipped_horizontal_image)
    cv2.imshow("flipped_vertical_image",flipped_vertical_image)
    cv2.imshow("flipped_both_image",flipped_both_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
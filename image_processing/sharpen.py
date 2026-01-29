import cv2
import numpy as np

image = cv2.imread("sanjay.jpg")

if image is None:
    print("opps! image not found")

else:
    resized_image = cv2.resize(image,(500,800))
    kernel = np.array([[0, -1, 0 ],
                       [-1, 5, -1],
                       [0, -1, 0]])
    
    sharpen_image = cv2.filter2D(resized_image, -1, kernel)
    cv2.imshow("original image",resized_image)
    cv2.imshow("sharpen image",sharpen_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread("sanjay.jpg",cv2.IMREAD_GRAYSCALE)
resized_img = cv2.resize(image,(500,800))
face = face_cascade.detectMultiScale(resized_img,1.08,2)
if len(face) == 0: 
    print("No faces detected!")
else:
    for  (x,y,w,h) in face:
        cv2.rectangle(resized_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        y1 = max(0, y-30)
        y2 = min(resized_img.shape[0], y+h+30)
        x1 = max(0, x-30)
        x2 = min(resized_img.shape[1], x+w+30)
        cropped_img = resized_img[y1:y2,x1:x2]
        profile = cv2.resize(cropped_img, (200, 200))
        break
    cv2.imshow("original_image",resized_img)
    cv2.imshow("cropped_image",profile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


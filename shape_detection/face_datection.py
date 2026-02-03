import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    res,frame = cap.read()
    flipped_image = cv2.flip(frame,1)
    gray = cv2.cvtColor(flipped_image,cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in face:
        cv2.rectangle(flipped_image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("face",flipped_image)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


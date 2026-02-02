import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

camera = cv2.VideoCapture(0)

while True:

    ret,frame = camera.read()
    if ret:
        flipped_image =  cv2.flip(frame,1)
        gray_image = cv2.cvtColor(flipped_image,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_image,1.1,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(flipped_image,(x,y),(x+w,y+h),(0,255,0),2)

            retgray = gray_image[y:y+h,x:x+w]
            retcolor = flipped_image[y:y+h,x:x+w]

            # eyes = eye_cascade.detectMultiScale(retgray,1.1,5)
            # if len(eyes) > 0:
            #      cv2.putText(flipped_image,"eyes detected",(x,y-40),1,cv2.FONT_HERSHEY_COMPLEX  ,(255,0,255),2)

            smile = smile_cascade.detectMultiScale(retgray,1.1,5)
            if len(smile) > 0:
                cv2.putText(flipped_image,"you are smiling",(x,y-20),1,cv2.FONT_HERSHEY_COMPLEX  ,(0,0,255),2)


        cv2.imshow("emotion detection",flipped_image)
        if cv2.waitKey(1) & 0xff == ord('q'):
            print("quitting")
            break
camera.release()
cv2.destroyAllWindows()
        
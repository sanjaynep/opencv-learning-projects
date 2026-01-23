import cv2 

image = cv2.imread("sanjay.jpg")
if image is None:
    raise FileNotFoundError("image not found")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("if you want to show type show and if you want to save type save")
user_input=str(input("please tell your choice:  "))
if (user_input == "show"):
        resized_image=cv2.resize(gray_image,(400,400))
        cropped_image=resized_image[20:300,40:350]
        cv2.imshow("croppedimage",cropped_image)
        cv2.imshow("sanjay",resized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

elif(user_input=="save"):
     output_name=input("please provide output name: ")
     cv2.imwrite(f"{output_name}.jpg",gray_image)
else:
      print("your choice doesnot match any field")


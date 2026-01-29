import cv2
import os

def drawing():
    path=input("enter image path: ").strip()

    if path.startswith("'") and path.endswith("'"):
        path = path[1:-1]
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]
    
    if os.path.exists(path):
        image = cv2.imread(path)
        if image is None:
            print("opps image not found.")
        else:
            resized_image = cv2.resize(image,(600,600))
            print("provide the choices you want to do in image \n 1. Add line \n 2. Add rectangle \n 3. Add circle \n 4. Add text")
            choice = int(input("Enter your choice 1,2,3 or 4: "))
            
            if choice == 1:
                x1 = int(input("Enter the x1 point between 0 to 600: "))
                y1 = int(input("Enter y1 point between 0 to 600: "))
                x2 = int(input("Enter x2 point between 0 to 600: "))
                y2 = int(input("Enter y2 point between 0 to 600: "))
                thickness = int(input("enter thickness of line in pixels: "))
                l1 = (x1,y1)
                l2 = (x2,y2)
                cv2.line(resized_image,l1,l2,(0,255,0),thickness)
            

            elif choice == 2:
                x1 = int(input("Enter the top left x1 point between 0 to 600: "))
                y1 = int(input("Enter top left y1 point between 0 to 600: "))
                x2 = int(input("Enter the bottom right x2 point between 0 to 600: "))
                y2 = int(input("Enter the bottom right y2 point between 0 to 600: "))
                thickness = int(input("enter thickness of line in pixels: "))
                l1 = (x1,y1)
                l2 = (x2,y2)
                cv2.line(resized_image,l1,l2,(0,255,0),thickness)

            elif choice == 3:
                x1 = int(input("enter the x1 point of center between 0 to 600: "))
                y1 = int(input("Enter the y1 point of center between 0 to 600: "))
                radius = int(input("Enter the radius in pixels: "))
                thickness = int(input("Enter the thickness in positive integer and to fill colour enter it in negative: "))
                center = (x1,y1)
                cv2.circle(resized_image,center,radius,color=(0,255,0),thickness=thickness)

            elif choice == 4:
                text = input("Enter the text you want to enter in image: ")
                x1 = int(input("enter x value of origin between 0 to 600: "))
                y1 = int(input("Entert y value of origin between 0 to 600: "))
                org = (x1,y1)
                size =  int(input("enter the font size must be bigger then 0: "))
                thickness = int(input("Enter the thickness value: "))
                cv2.putText(resized_image,text,org,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,size,(248,135,135),thickness)

            else:
                print("Incorrect choice. please enter between 1 and 4: ")

            cv2.imshow("your_image",resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return
    else:
        print("path not found")
        
drawing()

    


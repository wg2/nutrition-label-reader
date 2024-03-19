import CharacterRecognition
import cv2
from tkinter import *

def newWindow(map):
    window = Tk()
    window.title("Nutrition Label Display")
    header = Label(window, text="Press Space to Capture\nPress esc to exit\nCategory: Value")
    header.grid(row=0, column=0, columnspan=8)
    
    update(window, map)

def update(window, map):
    i = 3
    for key in map:
        label = Label(window, text=key + ": " + str(map[key]))
        label.grid(row=i, column=0, columnspan=8)
        i += 1
    window.mainloop()

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    reader = CharacterRecognition
    cv2.namedWindow("test")


    img_counter = 0
    map = {
        "Calories": 0,
        "Total Fat": 0,
        "Saturated Fat": 0,
        "Trans Fat": 0,
        "Cholesterol": 0,
        "Sodium": 0,
        "Total Carbohydrate": 0,
        "Dietary Fiber": 0,
        "Sugars": 0,
        #"- Includes": 0,
        "Protein": 0,
        "Vitamin D": 0,
        "Calcium": 0,
        "Iron": 0,
        "Potassium": 0
    }
    #window = newWindow(map)
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            reader.readNutritionLabel(image=frame, map=map)
            #update(window=window, map=map)
            newWindow(map)
            map = {
                "Calories": 0,
                "Total Fat": 0,
                "Saturated Fat": 0,
                "Trans Fat": 0,
                "Cholesterol": 0,
                "Sodium": 0,
                "Total Carbohydrate": 0,
                "Dietary Fiber": 0,
                "Sugars": 0,
                #"- Includes": 0,
                "Protein": 0,
                "Vitamin D": 0,
                "Calcium": 0,
                "Iron": 0,
                "Potassium": 0
            }
            # img_name = "opencv_frame_{}.png".format(img_counter)
            # cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            img_counter += 1


    cam.release()

    cv2.destroyAllWindows()
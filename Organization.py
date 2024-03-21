import CharacterRecognition
import cv2
from tkinter import *

# Behavior: Creates a new window with the information about controls and
#           loads the nutrition variables into the window
# 
# Exceptions: None
#
# Returns: None
#
# Parameters: A dictionary with the nutrtion labels inside
def newWindow(map):
    window = Tk()
    window.title("Nutrition Label Display")
    header = Label(window, text="Press Space to Capture\nPress esc to exit\nCategory: Value")
    header.grid(row=0, column=0, columnspan=8)
    
    update(window, map)

# Behavior: Updates the window with the new dictionary and resets it
#
# Exceptions: None
#
# Returns: None
#
# Parameters: A window object and a dictionary with the nutrition facts
def update(window, map):
    i = 3

    # Iterates through the dictionary and adds the contents as labels to the map
    for key in map:
        label = Label(window, text=key + ": " + str(map[key]))
        label.grid(row=i, column=0, columnspan=8)
        i += 1

    # Displays the window
    window.mainloop()

# Main method
# Before running please add a OpenAI key to CharacterRecognition.py
if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    reader = CharacterRecognition
    cv2.namedWindow("test")

    
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
        "Protein": 0,
        "Vitamin D": 0,
        "Calcium": 0,
        "Iron": 0,
        "Potassium": 0
    }
    
    # Shows the camera and allows a user to read a label shown through their webcam
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        # Gets what key was pressed
        k = cv2.waitKey(1)

        # If it is esc it ends the program
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        # If the key is space, it reads the label and opens a new window with the nutrition information
        elif k%256 == 32:
            # SPACE pressed
            reader.readNutritionLabel(image=frame, map=map)
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
                "Protein": 0,
                "Vitamin D": 0,
                "Calcium": 0,
                "Iron": 0,
                "Potassium": 0
            }


    cam.release()

    cv2.destroyAllWindows()

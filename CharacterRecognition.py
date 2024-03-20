import pytesseract
import cv2
import langchain
import langchain_core
import langchain_community
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.prompts.prompt import PromptTemplate
import openai
import os

# Place OpenAI API key here
os.environ["OPENAI_API_KEY"] = ""
llm = OpenAI()
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'




(# def extractFromImage(image_path):
#     # Load the image
#     image = cv2.imread(image_path)

#     # Convert the image to gray scale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#     # Use tesseract to do OCR on the image
#     text = pytesseract.image_to_string(thresh)

#     # Print the text
#     print(text)

#     return text
# def readNutritionLabel(imagePath, map):
#     if map == None:
#         map = {
#             "Calories": 0,
#             "Total Fat": 0,
#             "Saturated Fat": 0,
#             "Trans Fat": 0,
#             "Cholesterol": 0,
#             "Sodium": 0,
#             "Total Carbohydrate": 0,
#             "Dietary Fiber": 0,
#             "Sugars": 0,
#             #"- Includes": 0,
#             "Protein": 0,
#             "Vitamin D": 0,
#             "Calcium": 0,
#             "Iron": 0,
#             "Potassium": 0
#         }
#     text = extractFromImage(imagePath)
#     prompt = PromptTemplate(
#         input_variables=["nutritionLabel"], template="Please organize this nutrition label: {nutritionLabel} into the format nutrient: value. Do not include any non alphanumeric characters except :"# For example, Calories:100 or Total Fat:10. On numbers with units, use the mass, not percent value"
#     )

#     formatted = prompt.format(nutritionLabel=text)
#     chain = LLMChain(prompt=prompt, llm=llm)
#     text = chain.run(formatted)
#     print(text)
#     for line in text.split('\n'):
#         if map.keys().__contains__(line.split(':')[0]):
#             if line.__contains__("%") == False:
#                 if line.split(":")[1].__contains__("m"):
#                     val = line.split(': ')[1].split('m')[0]
#                 else:
#                     val = line.split(': ')[1].split('g')[0]
#                 map.update({line.split(':')[0]: (int(val)+  int(map.get(line.split(':')[0])))})
#                 print(map.get(line.split(':')[0]))
) 


def extractFromImage(image):
    # Convert the image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Use tesseract to do OCR on the image
    text = pytesseract.image_to_string(thresh, config="configFile.txt")

    # Print the text
    print(text)

    return text

def readNutritionLabel(image, map):
    if map == None:
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
    text = extractFromImage(image=image)
    prompt = PromptTemplate(
        input_variables=["nutritionLabel"], template="Please organize this nutrition label: {nutritionLabel} into the format nutrient: value. Do not include any non alphanumeric characters except for a colon. Do not include the percent of daily value. Do not use any decimals either, only whole numbers\n" +
        "the entire format is # For example, Calories: #\n Total Fat: #\n Saturated Fat: #\n Trans Fat: #\n Cholesterol: #\n Sodium: #\n Total Carbohydrate: #\n Dietary Fiber: #\n Sugars: #\n Protein: #\n Vitamin D: #\n Calcium: #\n Iron: #\n Potassium: #"
    )

    formatted = prompt.format(nutritionLabel=text)
    chain = LLMChain(prompt=prompt, llm=llm)
    text = chain.run(formatted)
    print(text)
    for line in text.split('\n'):
        if map.keys().__contains__(line.split(':')[0]):
            if line.__contains__("%") == False:
                if line.split(":")[1].__contains__("m"):
                    val = line.split(': ')[1].split('m')[0]
                else:
                    val = line.split(': ')[1].split('g')[0]
                map.update({line.split(':')[0]: (int(val)+  int(map.get(line.split(':')[0])))})
                print(map.get(line.split(':')[0]))


if __name__ == "__main__":
    
    path = r"C:\Users\khanw\OneDrive\Documents\GitHub\nutrition-label-reader\nutritionlabel.jpg"
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
    
    
    readNutritionLabel(path, map)
    print(map)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





# Load the image
    #image = cv2.imread(r"C:/Users/khanw/OneDrive/Documents/GitHub/nutrition-label-reader/nutritionlabel.jpg")



# image = cv2.imread(r"C:\Users\khanw\OneDrive\Documents\GitHub\nutrition-label-reader\nutritionlabel.jpg")
# if (image is None):
#     print("fuck")

#     # Display the image
# else:
#     cv2.imshow("Input", image)
#     # Convert the image to gray scale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#         # Use tesseract to do OCR on the image
#     text = pytesseract.image_to_string(thresh)

#         # Print the text
#     print(text)

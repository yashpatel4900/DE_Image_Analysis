import numpy as np
import cv2
import os

def gray_converter(train_img):

    number = train_img[6:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Train_img\train_'+ number)

    # Converts to Grayscale Image
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Save Image
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Grayscale'
    cv2.imwrite(os.path.join(path, 'grayscale_' +
                             number), img_grayscale)
    

def binary_converter(gray_img):
    
    number = gray_img[10:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Grayscale\grayscale_'+ number)

    # Converts to Complement of Binary
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY_INV)

    # Save Image
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Binary'
    cv2.imwrite(os.path.join(path, 'binary_' +
                             number), blackAndWhiteImage)
    

def dilation(binary_img):
    
    number = binary_img[7:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Binary\binary_'+ number)

    kernel = np.ones((3,3), np.uint8)
    img_dilation = cv2.dilate(img, kernel, iterations=1) 

    # Save Image
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Dilated_Img'
    cv2.imwrite(os.path.join(path, 'dilated_' + number), img_dilation)


def eroding(dilated_img):
    
    number = dilated_img[8:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Dilated_Img\dilated_'+ number)

    kernel = np.ones((3,3), np.uint8)
    img_erosion = cv2.erode(img, kernel, iterations=1) 

    # Save Image
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Eroded_Img'
    cv2.imwrite(os.path.join(path, 'eroded_' + number), img_erosion)

# RGB to Grayscale Image
entries = os.listdir('Train_img/')
for entry in entries:
    gray_converter(entry)

# Grayscale Image to Complement of Binary Image
entries = os.listdir('Grayscale/')
for entry in entries:
    binary_converter(entry)

# Binary Image to Dilated Image
entries = os.listdir('Binary/')
for entry in entries:
    dilation(entry)

# Dilated Image to Eroded Image
entries = os.listdir('Dilated_Img/')
for entry in entries:
    eroding(entry)


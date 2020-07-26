import numpy as np
import cv2
import os

def gray_converter(train_img):

    number = train_img[6:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Train_img\train_'+ number)
    # height, width, channel = img.shape
    img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Grayscale'
    cv2.imwrite(os.path.join(path, 'grayscale_' +
                             number), img_grayscale)
    
    # cv2.imshow('image', img_grayscale)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def binary_converter(gray_img):
    
    number = gray_img[10:]
    img = cv2.imread(r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Grayscale\grayscale_'+ number)
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    path = r'C:\Users\india\Desktop\Yash\DE_Image_Analysis\Binary'
    cv2.imwrite(os.path.join(path, 'binary_' +
                             number), blackAndWhiteImage)
    
    # cv2.imshow('image', blackAndWhiteImage)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


entries = os.listdir('Train_img/')
for entry in entries:
    gray_converter(entry)

entries = os.listdir('Grayscale/')
for entry in entries:
    binary_converter(entry)
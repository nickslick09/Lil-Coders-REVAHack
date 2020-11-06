# from cv2 import cv2 
   
      
# # test image 
# image = cv2.imread('applet.jpg') 
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# histogram = cv2.calcHist([gray_image], [0],  
#                          None, [256], [0, 256]) 
   
# # data1 image 
# image = cv2.imread('apple0.jpg') 
# gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# histogram1 = cv2.calcHist([gray_image1], [0],  
#                           None, [256], [0, 256]) 
   
# # data2 image 
# image = cv2.imread('applet - Copy.jpg') 
# gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# histogram2 = cv2.calcHist([gray_image2], [0],  
#                           None, [256], [0, 256]) 
   
   
# c1, c2 = 0, 0
   
# # Euclidean Distace between data1 and test 
# i = 0
# while i<len(histogram) and i<len(histogram1): 
#     c1+=(histogram[i]-histogram1[i])**2
#     i+= 1
# c1 = c1**(1 / 2) 
   
  
# # Euclidean Distace between data2 and test 
# i = 0
# while i<len(histogram) and i<len(histogram2): 
#     c2+=(histogram[i]-histogram2[i])**2
#     i+= 1
# c2 = c2**(1 / 2) 
   
# if(c1<c2): 
#     print("data1.jpg is more similar to test.jpg as compare to data2.jpg") 
#     print(c1)
#     print(c2)
# else: 
#     print("data2.jpg is more similar to test.jpg as compare to data1.jpg") 


#Import Necessary Packages
from cv2 import cv2
from MappingLetters import MapLetters as Mapping
from captchaWriter import CaptchaWriter
import numpy as np

captchaFilename = "black.white-fa73n.jpg"
captchaImage = cv2.imread(captchaFilename)
captchaImageGray = cv2.cvtColor(captchaImage, cv2.COLOR_BGR2GRAY) 

width, height = captchaImageGray.shape[::-1] 

captchaCropped = captchaImageGray
letter = captchaImageGray[0:height,0:50]

print(CaptchaWriter.captchaResult(captchaCropped,letter))

cv2.waitKey(0)
cv2.destroyAllWindows()

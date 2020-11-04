# import the necessary packages
from cv2 import cv2
# load the image and show it
image = cv2.imread("‪Captcha (1).png")
cv2.imshow("original", image)
cv2.waitKey(0)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from cv2 import cv2
from MappingLetters import MapLetters as Mapping
from captchaWriter import CaptchaWriter
from BlackNWhite import BlacknWhite
import numpy as np
PATH=("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(PATH)
file_object = open('currentuserdetails.txt', 'r')
Lines = file_object.readlines() 
x=[]
for line in Lines:
    y=line.split()
    x.append(y)
uname=x[0]
pw=x[1]
emailid=x[2]
file_object.close()
driver.get('https://erp.reva.edu.in/REVAUniversity/StudentLogin.do')
username=driver.find_element_by_name("userName")
username.clear()
username.send_keys(uname)
password=driver.find_element_by_name("password")
password.clear()
password.send_keys(pw)
image=driver.find_element_by_xpath('//*[@id="captcha"]').screenshot('captcha.png') # saves screenshot
filename = "captcha.png"
BlacknWhite.TurnBlacknWhite(filename)

captchaFilename = filename[:-4]+"_bw"+filename[-4:]
captchaImage = cv2.imread(captchaFilename)
captchaImageGray = cv2.cvtColor(captchaImage, cv2.COLOR_BGR2GRAY) 

width, height = captchaImageGray.shape[::-1] 

captchaCropped = captchaImageGray
letter = captchaImageGray[0:height,0:50]

capval=(CaptchaWriter.captchaResult(captchaCropped,letter))
print(capval)
cap=driver.find_element_by_name("captchaValue")
cap.clear()
cap.send_keys(capval)
cv2.waitKey(0)
cv2.destroyAllWindows()
driver.find_element_by_id("Login").click()
#driver.quit() #for closing the browser

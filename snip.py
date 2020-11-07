from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DecodingCaptcha import Decode
import time
from cv2 import cv2
from MappingLetters import MapLetters as Mapping
from captchaWriter import CaptchaWriter
from BlackNWhite import BlacknWhite
import numpy as np
import PIL
from PIL import Image
import os
import smtplib
import imghdr
from email.message import EmailMessage
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
driver.maximize_window()

captchaName = 'captcha.png'
image=driver.find_element_by_xpath('//*[@id="captcha"]').screenshot(captchaName) # saves screenshot
decodedCaptcha = Decode.getCaptcha(captchaName)
username=driver.find_element_by_name("userName")
username.clear()
username.send_keys(uname)
password=driver.find_element_by_name("password")
password.clear()
password.send_keys(pw)
print(decodedCaptcha)
cap=driver.find_element_by_name("captchaValue")
cap.clear()
cap.send_keys(decodedCaptcha)

driver.find_element_by_id("Login").click()

driver.get('https://erp.reva.edu.in/REVAUniversity/studentWiseAttendanceSummary.do?method=getIndividualStudentWiseSubjectAndActivityAttendanceSummary')
driver.execute_script("document.body.style.zoom='77%'")
driver.get_screenshot_as_file("Screenshot.jpg")
img=Image.open("Screenshot.jpg")
area=(210,100,1145,600)
img_crop=img.crop(area)
#img_crop.show()
crop=img_crop.convert('RGB')
crop.save('Attendance.png')
#driver.quit() #for closing the browser

EMAIL_ADDRESS='pingttendance@gmail.com'
EMAIL_PASSWORD='pingttendance@333'
msg = EmailMessage()
msg['Subject'] = 'Welcome to Pingttendance, here is your Attendance!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = x[2]

msg.set_content('Check the attachment for your Attendance details')

with open('Attendance.png','rb') as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

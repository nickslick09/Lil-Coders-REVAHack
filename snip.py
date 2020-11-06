from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DecodingCaptcha import Decode
import time
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

captchaName = 'captcha.png'
image=driver.find_element_by_xpath('//*[@id="captcha"]').screenshot(captchaName) # saves screenshot

decodedCaptcha = Decode.getCaptcha(captchaName)
print(decodedCaptcha)

cap=driver.find_element_by_name("captchaValue")
cap.clear()
cap.send_keys(decodedCaptcha)
driver.find_element_by_id("Login").click()
driver.quit() #for closing the browser

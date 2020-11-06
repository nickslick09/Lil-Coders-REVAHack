from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
image=driver.find_element_by_xpath('//*[@id="captcha"]').screenshot('captcha.png') # saves screenshot
driver.find_element_by_id("Login").click()
#driver.quit() #for closing the browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time
PATH=("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.get('https://erp.reva.edu.in/REVAUniversity/StudentLogin.do')
username=driver.find_element_by_name("userName")
username.clear()
username.send_keys("R18CS343")
password=driver.find_element_by_name("password")
password.clear()
password.send_keys("xxxxxx")
image=driver.find_element_by_xpath('//*[@id="captcha"]').screenshot('captcha.png') # saves screenshot
driver.find_element_by_id("Login").click()
#driver.quit() for closing the browser

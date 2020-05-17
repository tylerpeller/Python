from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import csv


#retrieve login info from file
with open("c:/Users/tyler/OneDrive/Documents/Python_Scripts/Leumi.txt" ,"r") as login:
    user = login.readline()
    passwd = login.readline()


driver = webdriver.Chrome('c:/Users/tyler/OneDrive/Documents/Python_Scripts/chromedriver')
driver.get('https://lms.schwab.com/Login/Full?clientId=schwab-mweb&mobile=yes&redirecturi=client.schwab.com/login/signon/authcodehandler.ashx&returnUrl=/')
# frame = driver.find_element_by_css_selector('div.tool_forms iframe')
# driver.switch_to.frame(frame)
t.sleep(5.5)

#fill in username                       
username = driver.find_element_by_id('LoginId')
username.send_keys("user")
t.sleep(1.5)

#fill in password
password = driver.find_element_by_id('Password')
password.send_keys("passwd")
password.send_keys(Keys.ENTER)

email = driver.find_element_by_xpath("//input[@id='EmailId']")
email.click()

##next step = pull trade/history info into excel
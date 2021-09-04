#this is UpTime_robot.py for automation function
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

mydriver=webdriver.Firefox()
mydriver.get("https://uptimerobot.com/")
Application_Manager_NOC=webdriver.Firefox()
Application_Manager_NOC.get("192.168.15.247:9090")
#print(mydriver.title)
#print(mydriver.current_url)
mydriver.close()
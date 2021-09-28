from selenium import webdriver as wd 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import urllib.request
from socket import timeout
from urllib.error import HTTPError, URLError
import socket
import ntplib
from time import ctime
import getpass
import urllib.request
import datetime as DT

timeout = 5    
page_index = 0
 
def login (firefox_webdriver, link, username_element_ID, username, password_element_ID, password, login_button_ID):
    global page_index
    global timeout
    if page_index > 0: 
        firefox_webdriver.execute_script("window.open('{}');".format(link))
    else: 
        firefox_webdriver.get(link)
    MENOC_handles = firefox_webdriver.window_handles[page_index]
    page_index = page_index + 1
    
    try:
        element_present = EC.presence_of_element_located((By.ID, login_button_ID))
        WebDriverWait(firefox_webdriver, timeout).until(element_present)
    
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")
    username0 = firefox_webdriver.find_element_by_name(username_element_ID)
    username0.send_keys(username)
    print (username0)
    password0 = firefox_webdriver.find_element_by_name(password_element_ID)
    password0.send_keys(password)
    print (password0)
    DomainOption = firefox_webdriver.find_element(By.ID,"domainOptions")
    DO = Select(DomainOption)
    DO.select_by_value("1")
    Ok_firefox_webdriver = firefox_webdriver.find_element_by_name(login_button_ID).click()
    firefox_webdriver.switch_to.window(MENOC_handles) 
        
    #print ("Manage Engine NOC is stated")
    

frfx = wd.Firefox()
login (frfx, "http://192.168.15.247:9090/MyPage.do?method=viewDashBoard&toredirect=true", "username", "vnc_monitor", "j_password", "monitor", "submit")
login (frfx, "http://192.168.15.247:9090/MyPage.do?method=viewDashBoard&toredirect=true", "username", "vnc_monitor", "j_password", "monitor", "submit")

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

now = DT.datetime.now()
hour = now.hour
target_hour = now.hour + 12

print(now)

CurrnetUser=getpass.getuser()
print(CurrnetUser + " " + "Is Online")

# Manage Engine NOC -->> MENOC
Login = wd.Firefox()
timeout = 5
MENOC = Login.get("http://192.168.15.247:9090/MyPage.do?method=viewDashBoard&toredirect=true")
MENOC_handles = Login.window_handles[0]
username0 = Login.find_element_by_name("username")
username0.send_keys("vnc_monitor")
password0 = Login.find_element_by_name("j_password")
password0.send_keys("monitor")
DomainOption = Login.find_element(By.ID,"domainOptions")
DO = Select(DomainOption)
DO.select_by_value("1")
Ok_Login = Login.find_element_by_name("submit").click()
print ("Manage Engine NOC is stated")
time.sleep(2)

# Manage Engine Eniac -->> MEE
link = "http://10.10.10.63:9090/MyPage.do?method=viewDashBoard&toredirect=true"
Login.execute_script("window.open('{}');".format(link))
MEE_handles = Login.window_handles[1]
#driver.switch_to.window(window_after)
Login.switch_to.window(MEE_handles)
time.sleep(3)
username1 = Login.find_element_by_name("username")
username1.send_keys("vnc_monitor")
password1 = Login.find_element_by_name("j_password")
password1.send_keys("monitor")
DomainOption = Login.find_element(By.ID,"domainOptions")
DO = Select(DomainOption)
DO.select_by_value("1")
Ok_Login = Login.find_element_by_name("submit").click()
print("Manage Engine Eniac is started")
time.sleep(2)

# Solarwinds Orion NOC -->> SONOC

link = "http://192.168.15.253/Orion/Login.aspx"
Login.execute_script("window.open('{}');".format(link))
SONOC_handles = Login.window_handles[2]
#driver.switch_to.window(window_after)
Login.switch_to.window(SONOC_handles)
time.sleep(3)
username2 = Login.find_element(By.ID,"ctl00_BodyContent_Username")
username2.send_keys("vnc_monitor")
password2 = Login.find_element(By.ID,"ctl00_BodyContent_Password")
password2.send_keys("monitor")
time.sleep(1)
Ok_Login = Login.find_element_by_xpath("/html/body/div/div[1]/form/div[3]/div[2]/div/div[3]/a").click()
print("Solarwinds Orion NOC is started")
time.sleep(2)

# Solarwinds Orion Eniac -->> SOE

link = "http://10.10.10.64/Orion/Login.aspx"
Login.execute_script("window.open('{}');".format(link))
SOE_handles = Login.window_handles[3]
#driver.switch_to.window(window_after)
Login.switch_to.window(SOE_handles)
time.sleep(3)
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(Login, timeout).until(element_present)

except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
username2 = Login.find_element(By.ID,"ctl00_BodyContent_Username")
username2.send_keys("vnc_monitor")
password2 = Login.find_element(By.ID,"ctl00_BodyContent_Password")
password2.send_keys("monitor")
time.sleep(1)
Ok_Login = Login.find_element_by_xpath("/html/body/div/div[1]/form/div[3]/div[2]/div/div[3]/a").click()
print("Solarwinds Orion Eniac is started")

# Oracle Enterprise Manager -->> cctrl

link = "https://cctrl.eniac-tech.local:7803/em/faces/logon/core-uifwk-console-login"
Login.execute_script("window.open('{}');".format(link))
CCTRL_handles = Login.window_handles[4]
Login.switch_to.window(CCTRL_handles)
time.sleep(3)
username2 = Login.find_element(By.ID,"j_username::content")
username2.send_keys("emadmin")
password2 = Login.find_element(By.ID,"j_password::content")
password2.send_keys("em@dm!n")
time.sleep(1)
Ok_Login = Login.find_element(By.ID,"login").click()
time.sleep(2)
print("Oracle Enterprise Manager is started")

# Respina Monitor -->> RM
link = "https://monitor.respina.net"
Login.execute_script("window.open('{}');".format(link))
RM_handles = Login.window_handles[5]
Login.switch_to.window(RM_handles)
time.sleep(3)
username2 = Login.find_element_by_name("login_username")
username2.send_keys("eniac")
password2 = Login.find_element_by_name("login_password")
password2.send_keys("eniac59")
time.sleep(1)
Ok_Login = Login.find_element_by_xpath("/html/body/div/div[2]/span/form/input[4]").click()
time.sleep(2)
print("Respina Monitor is started")

# MabnaTelecom Monitor -->> MTM

link = "http://monitoring.mabnatelecom.com"
Login.execute_script("window.open('{}');".format(link))
MTM_handles = Login.window_handles[6]
Login.switch_to.window(MTM_handles)
try:
    status_code = "wait for get code from URL"
    maberror = "No Error"
    print (status_code)
    status_code = urllib.request.urlopen(link).getcode()
    print (status_code)
except HTTPError as e:
    print (maberror)
    #maberror = e.code
if status_code == 200:
    print("MabnaTelecom is up")
    time.sleep(5)
    username = Login.find_element_by_name("login_username")
    username.send_keys("eniac-rayaneh")
    password = Login.find_element_by_name("login_password")
    password.send_keys("eniac59")
    time.sleep(1)
    Ok_Login = Login.find_element_by_xpath("/html/body/form/table/tbody/tr[8]/td/input").click()
    time.sleep(2)
    print("MabnaTelecom Monitor is started")
else:
    #print (status_code)
    print (maberror)
    print ("MabnaTelecom Monitoring is not available")

time.sleep(4)

# NMS
link = "http://192.168.15.227/map.php?I_SessionId=ebdfb7d4100ba8c10c30735aeb1af474"
Login.execute_script("window.open('{}');".format(link))
NMS_handles = Login.window_handles[7]
Login.switch_to.window(NMS_handles)
print("NMS is started")
time.sleep(2)

# UPS monitoring MT2K20 -->> UPS20
link = "http://10.10.10.249/index.html"
Login.execute_script("window.open('{}');".format(link))
UPS20_handles = Login.window_handles[8]
Login.switch_to.window(UPS20_handles)
print("UPS20 monitoring is started")
time.sleep(2)

#UPS monitoring MST40 -->> UPS40
link = "http://10.10.10.250/index.html"
Login.execute_script("window.open('{}');".format(link))
UPS40_handles = Login.window_handles[9]
Login.switch_to.window(UPS40_handles)
print("UPS40 monitoring is started")
time.sleep(5)

# UP time robot -->> UPTR
link = "https://uptimerobot.com/login"
Login.execute_script("window.open('{}');".format(link))
UPTR_handles = Login.window_handles[10]
Login.switch_to.window(UPTR_handles)
time.sleep(3)
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(Login, timeout).until(element_present)

except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
username = Login.find_element(By.ID,"userEmail")
username.send_keys("sspoormosavi@gmail.com")
password = Login.find_element(By.ID,"userPassword")
password.send_keys("123456@a")
time.sleep(1)
Ok_Login = Login.find_element_by_xpath("/html/body/section/div/div[2]/div[1]/form[1]/button").click()
time.sleep(2)
print("uptimerobot is started")

# Zabbix Monitoring -->>ZM
link = "http://192.168.15.245/zabbix"
Login.execute_script("window.open('{}');".format(link))
ZM_handles = Login.window_handles[11]
Login.switch_to.window(ZM_handles)
time.sleep(3)
username = Login.find_element(By.ID,"name")
username.send_keys("MonitoringD")
password = Login.find_element(By.ID,"password")
password.send_keys("MonitoringD")
time.sleep(1)
Ok_Login = Login.find_element(By.ID,"enter").click()
time.sleep(2)
print("Zabbix Monitoring is started")

##### switch between tabs automaticly
Login.switch_to.window(MENOC_handles)
size = len(Login.window_handles)
print (size)
while hour < target_hour:
    for i in range(size):
        if Login.window_handles[i] != ZM_handles:
            Login.switch_to.window(Login.window_handles[i])
            time.sleep(6)
        elif Login.window_handles[i] == ZM_handles:
            Login.switch_to.window(ZM_handles)
            time.sleep(6)
            i = 0

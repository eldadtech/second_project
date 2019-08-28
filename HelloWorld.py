from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
# get chrome driver
driver = webdriver.Chrome(executable_path="C:\\code\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(5)
# Enter the Site
driver.get("http://192.168.99.101:5000/")
time.sleep(5)
driver.close()
driver.quit()
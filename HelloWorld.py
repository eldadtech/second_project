from selenium import webdriver
def end_automation(driver):
    time.sleep(2)  # just to view the result before closing
    driver.close()
    driver.quit()


#from selenium.webdriver.common.keys import Keys
import time
import logging
LOGGER = logging.getLogger('Error')  # initiate logger

# get chrome driver
driver = webdriver.Chrome(executable_path="C:\\code\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(20)
# Enter the Site
try:
    driver.get("http://192.168.99.101:5000/")
# time.sleep(10)
   # hello_text = driver.find_element_by_tag_name('pre')
    hello_text = driver.find_element_by_xpath("/html//body")



    print(hello_text)

except BaseException as e:  # catch error and print it
    LOGGER.error("failed " + str(e))
finally:
    end_automation(driver)



from selenium import webdriver
import time
import logging
LOGGER = logging.getLogger('Error')  # initiate logger


def end_automation(driver):
    time.sleep(2)  # just to view the result before closing
    driver.close()
    driver.quit()


# get chrome driver
driver = webdriver.Chrome(executable_path="C:\\code\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
# Enter the Site
try:
    driver.get("http://192.168.99.101:5000/")
# Get the text and print to console
    hello_text = driver.find_element_by_xpath("/html//body")
    print(hello_text.text)

except BaseException as e:  # catch error and print it
    LOGGER.error("failed " + str(e))
finally:
    end_automation(driver)



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#launch Webdriver
browser = webdriver.Chrome()
#navigate to test automation practice page
browser.get('http://testautomationpractice.blogspot.com/')
time.sleep(5)
#maximize window
browser.maximize_window()
#click on element
browser.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)

# browser.switch_to.alert.accept()# to accept the alert
browser.switch_to.alert.dismiss()# to dismiss the alert
# browser.close

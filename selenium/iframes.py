from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#launch Webdriver
browser = webdriver.Chrome()
#navigate to seleniumhq page
browser.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
#wait for browser to load
wait=WebDriverWait(browser,5)
# switch to Frame by Name
browser.switch_to.frame('packageListFrame')
time.sleep(4)
#click on link within frame
browser.find_element_by_link_text('org.openqa.selenium').click()
#switch control to default parent window
browser.switch_to.default_content()
# switch to Frame by Name
browser.switch_to.frame('packageFrame')
time.sleep(4)
browser.find_element_by_link_text('WebDriver').click()
#switch control to default parent window
browser.switch_to.default_content()
# switch to Frame by Name
browser.switch_to.frame('classFrame')
time.sleep(4)
#click on link within frame
browser.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()
browser.close()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
#launch Webdriver
browser = webdriver.Chrome()
#navigate to test automation testing page
browser.get('http://demo.automationtesting.in/Windows.html')
wait=WebDriverWait(browser,5)
# click on element
browser.find_element_by_xpath('//*[@id="Tabbed"]/a').click()
#print current window handle
print('Parent window handle '+browser.current_window_handle)
#get all browser windows using window_handles property
handles=browser.window_handles
for handle in handles:
    #switch to the window using handle
    browser.switch_to.window(handle)
    # print current window handle
    print('Current window handle ' + browser.current_window_handle)
    # print current window title
    print('Current window Title ' + browser.title)
browser.quit()

import os
from selenium import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# get the path of ChromeDriverServer
from selenium.webdriver.support.select import Select
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
dir = os.path.dirname(__file__)
chrome_driver_path = r"D:\Praful\Python\PomDemo\resources\drivers" + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://advantageonlineshopping.com")
driver.find_element_by_id('menuUser').click()
wait = WebDriverWait(driver, 20)
element = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
driver.find_element_by_name('username').send_keys('vishal1117')
driver.find_element_by_name('password').send_keys('Vishal1117')
wait.until(EC.element_to_be_clickable((By.ID, 'sign_in_btnundefined')))
element=driver.find_element_by_id('sign_in_btnundefined')
driver.execute_script("arguments[0].click();", element)
element=driver.find_element_by_id('speakersTxt')
webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
driver.find_element_by_id('speakersLink').click()
driver.find_element_by_xpath("//a[contains(text(),'Bose SoundLink Wireless Speaker')]").click()
# driver.find_element_by_xpath("//span[@title='RED']").click()
# driver.find_element_by_name('quantity').send_keys('2')
driver.find_element_by_xpath("//button[@name='save_to_cart']").click()
driver.find_element_by_id('checkOutPopUp').click()
driver.find_element_by_id('next_btn').click()
driver.find_element_by_id("safepay_username").send_keys("Vishal1117")
driver.find_element_by_id("safepay_password").send_keys("Vishal1117")
driver.find_element_by_id("pay_now_btn_SAFEPAY").click()
tracking_element=driver.find_element_by_id("trackingNumberLabel")
orderno_element=driver.find_element_by_id("orderNumberLabel")
print(tracking_element.text)
print(orderno_element.text)

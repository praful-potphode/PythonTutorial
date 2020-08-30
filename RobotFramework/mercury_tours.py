import pandas as pd
import os
from pathlib import Path
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
testdata=None
def get_title():
    return "demo"

def initialiseddriver():
    chrome_driver_path = r"drivers/chromedriver_v83.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()
    BuiltIn().log(message="window launched")

    return driver
def launch_url(driver,url):
    BuiltIn().log(testdata)
    driver.get(testdata['url'])
    # driver.get(url)
def login(driver,uname,password):
    username=driver.find_element_by_name('userName').send_keys(uname)
    password=driver.find_element_by_name('password').send_keys(password)
    login=driver.find_element_by_name('login').click()

def book_ticket(driver):
    click_type = driver.find_elements_by_name('tripType')
    click_type[0].click()
    pass_count = Select(driver.find_element_by_name('passCount')).select_by_index(2)
    depart_stn = Select(driver.find_element_by_name('fromPort')).select_by_value('Frankfurt')
    depart_on = Select(driver.find_element_by_name('fromMonth')).select_by_visible_text('April')
    depart_at = Select(driver.find_element_by_name('fromDay')).select_by_value('4')

    serviceclass = driver.find_elements_by_name('servClass')
    serviceclass[1].click()

    arriving_stn = Select(driver.find_element_by_name('toPort'))
    arriving_stn.select_by_index(2)

    airline_pref = Select(driver.find_element_by_name('airline'))
    airline_pref.select_by_visible_text('Blue Skies Airlines')

    Returning_month = Select(driver.find_element_by_name('toMonth'))
    Returning_month.select_by_value('5')
    Select(driver.find_element_by_name('toDay')).select_by_value('3')

    cont = driver.find_element_by_name('findFlights')
    cont.click()

    flight_name = driver.find_elements_by_name('outFlight')
    flight_name[2].click()

    ret_flight_name = driver.find_elements_by_name('inFlight')
    ret_flight_name[2].click()
    contin = driver.find_element_by_name('reserveFlights')
    contin.click()


def passenger_details(driver):
    p1name = driver.find_element_by_name('passFirst0')
    p1name.send_keys('Praveen')
    p1lname = driver.find_element_by_name('passLast0')
    p1lname.send_keys('Singh')
    p1meal = Select(driver.find_element_by_name('pass.0.meal'))
    p1meal.select_by_index(3)

    p2name = driver.find_element_by_name('passFirst1')
    p2name.send_keys('Kumari')
    p2lname = driver.find_element_by_name('passLast1')
    p2lname.send_keys('Nidhi')
    p2meal = Select(driver.find_element_by_name('pass.1.meal'))
    p2meal.select_by_index(5)

    p2name = driver.find_element_by_name('passFirst2')
    p2name.send_keys('Rudraksh')
    p2lname = driver.find_element_by_name('passLast2')
    p2lname.send_keys('Rana')
    p2meal = Select(driver.find_element_by_name('pass.2.meal'))
    p2meal.select_by_index(6)

    card_type = Select(driver.find_element_by_name('creditCard')).select_by_visible_text('MasterCard')
    cardno = driver.find_element_by_name('creditnumber').send_keys('12345')
    expiration_date = driver.find_element_by_name('cc_exp_dt_mn').send_keys('12')
    expiration_year = driver.find_element_by_name('cc_exp_dt_yr').send_keys('2022')
    card_payee_firstname = driver.find_element_by_name('cc_frst_name').send_keys('Praveen')
    card_payee_midname = driver.find_element_by_name('cc_mid_name').send_keys('Kumar')
    card_payee_lastname = driver.find_element_by_name('cc_last_name').send_keys('Singh')
    ticketless = driver.find_element(By.NAME, 'ticketLess').click()
    address_billing = driver.find_element_by_name('billAddress1').send_keys('Mezza 9')
    address_city = driver.find_element_by_name('billCity').send_keys('Pune')
    address_State = driver.find_element_by_name('billState').send_keys('Maharashtra')
    address_pin = driver.find_element_by_name('billState').send_keys('411007')
    address_country = Select(driver.find_element_by_name('billCountry')).select_by_visible_text('INDIA')
    delivery_address = driver.find_element_by_name('ticketLess').click()
    secure = driver.find_element_by_name('buyFlights').click()
    log_out = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[3]/a').click()
def quit(driver):
    driver.quit()

def before_suite():
    os.environ['ROOT_DIR']=os.path.dirname(Path(os.path.abspath(__file__)))

def after_suite():
    BuiltIn().log('After suite')
def load_testcase_data(testcase_name):
    global testdata
    BuiltIn().log(str('loading data for    '+testcase_name))
    df=pd.DataFrame()
    df=pd.read_csv(os.environ['ROOT_DIR']+r'\data\testdata.csv')
    df=df[df['TESTNAME'] == testcase_name]
    testdata=dict(zip(df['PARAMETERNAME'],df['PARAMETERVALUE']))
    BuiltIn().log(str(testdata))
#close the browser window pass.0.meal
# driver=initialiseddriver()
# driver.get("http://newtours.demoaut.com/")
# login(driver,'mercury','mercury')
# book_ticket(driver)
# passenger_details(driver)
#driver.quit()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3708225053&keywords=marketing%20manager&refresh=true")
sign_in = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

email_or_phone = driver.find_element(By.ID,'username')
email_or_phone.send_keys('gimaildev@gmail.com')

password = driver.find_element(By.ID,'password')
password.send_keys('dreamHous')

submit_btn = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
submit_btn.click()
# search_btn =driver.find_element(By.XPATH,'//*[@id="global-nav-search"]/div/div[2]/button[1]')
# search_btn.click()

all_listing = driver.find_elements(By.CSS_SELECTOR, '.job-card-list__title')
for item in all_listing:
    print('called')
    item.click()
    try:

        easy_apply_btn = driver.find_element(By.XPATH,'//*[@id="ember321"]')
        easy_apply_btn.click()


        phone_number_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3708225053-96487651-phoneNumber-nationalNumber"]')
        phone_number_input.send_keys('9878778786')#this is the phone number
        phone_number_input.send_keys(Keys.ENTER)

    except NoSuchElementException:
        print('no application button skipped')



time.sleep(300)
from cmath import log
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome('./chromedriver.exe')
# driver.maximize_window()

driver.get('https://lottery1-intl.fwc22.tickets.fifa.com/lottery/welcome_es.html')

first_login_button = '//*[@id="login_block"]/div/div[2]/a'
cookies_button = '//*[@id="onetrust-accept-btn-handler"]'

# try:
cookies_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, cookies_button)))

must_accept_cookies = driver.find_element(By.XPATH, cookies_button)

# cookies_acepted = False
if (must_accept_cookies):
    must_accept_cookies.click()
    # cookies_acepted = True

WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, first_login_button))).click()

email_input = '//*[@id="signInName"]'
password_input = '//*[@id="password"]'
login_submit = '//*[@id="next"]'

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, email_input))).send_keys("matimassetti@hotmail.com")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, password_input))).send_keys("olimpo")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, login_submit))).click()

# except Exception as e:
#     print("Exception", e)
#     # driver.quit()

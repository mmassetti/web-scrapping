import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('./chromedriver.exe')

# USER AGENT?
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/80.0.3987.149 Safari/537.36

driver.get('https://account.fifa.com/5a7baeb7-e706-4830-ad9f-103eba126311/oauth2/v2.0/authorize?response_type=code&client_id=7c38bec6-36b1-4ed2-89d4-f80fb0984b0e&redirect_uri=https%3A%2F%2Flottery1-intl.fwc22.tickets.fifa.com%2Flottery%2Fsecure%2Foidc%2Fcallback&scope=7c38bec6-36b1-4ed2-89d4-f80fb0984b0e+openid+email+profile+offline_access&state=H_3Qx6T3dlgRDPHGxRqY40xc-pEtU663-TlZEiES6y4&display=page&p=B2C_1A_FIFA_SignUpOrSignIn&campaignId=ticketing&prompt=login')

email_input = '//*[@id="signInName"]'
password_input = '//*[@id="password"]'
login_submit = '//*[@id="next"]'

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, email_input))).send_keys("agusmassetti@gmail.com")
driver.find_element(By.XPATH, password_input).send_keys("Aurinegro741995m")


driver.find_element(By.XPATH, login_submit).click()

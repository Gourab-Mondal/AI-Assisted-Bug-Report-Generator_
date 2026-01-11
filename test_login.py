from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#cgrome or chromium setup
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # open the site
    driver.get("https://www.saucedemo.com")

    # locate the elements below
    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    # enter valid creds
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_btn.click()

    time.sleep(2)

    # verify login
    current_url = driver.current_url

    if "inventory" in current_url:
        print("✅ Login Test Passed")
    else:
        print("❌ Login Test Failed")

finally:
    time.sleep(3)
    driver.quit()

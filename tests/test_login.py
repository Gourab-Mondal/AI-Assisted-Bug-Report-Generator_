from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("standard_user", "secret_sauce")

        # Wait until inventory page loads
        wait.until(EC.url_contains("inventory"))

        # Proper assertion
        assert "inventory" in driver.current_url
        print("✅ Login Test Passed")

    finally:
        driver.quit()

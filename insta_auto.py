from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Setup logging
logging.basicConfig(filename='automation.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def log_and_print(message):
    print(message)
    logging.info(message)

def automate_instagram():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    try:
        log_and_print("Opening Instagram")
        driver.get('https://www.instagram.com/')
        wait = WebDriverWait(driver, 10)

        log_and_print("Logging in")
        element = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        username_field.send_keys('your_dummy_username')
        password_field.send_keys('your_dummy_password')
        password_field.send_keys(Keys.RETURN)
        
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
        log_and_print("Logged in successfully")

        log_and_print("Searching for 'cbitosc'")
        search_box = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search"]')
        search_box.send_keys('cbitosc')
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        if driver.find_elements(By.XPATH, '//button[text()="Follow"]'):
            follow_button = driver.find_element(By.XPATH, '//button[text()="Follow"]')
            follow_button.click()
            log_and_print("Followed 'cbitosc'")

        log_and_print("Extracting account data")
        account_name = driver.find_element(By.TAG_NAME, 'h1').text
        bio = driver.find_element(By.XPATH, '//div[contains(text(), "bio")]/following-sibling::span').text
        followers = driver.find_element(By.XPATH, '//a[contains(@href, "followers")]/span').text

        with open('cbitosc_data.txt', 'w') as file:
            file.write(f"Account Name: {account_name}\n")
            file.write(f"Bio: {bio}\n")
            file.write(f"Followers: {followers}\n")

    except Exception as e:
        log_and_print(f"An error occurred: {e}")

    finally:
        driver.quit()

if __name__ == '__main__':
    automate_instagram()
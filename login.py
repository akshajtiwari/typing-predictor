from dotenv import load_dotenv
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
load_dotenv()
def login():
    driver=webdriver.Chrome()
    driver.get("https://monkeytype.com/login")
    wait = WebDriverWait(driver, 15)
    # click accept cookies
    try:
        accept_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'accept')]")))
        driver.execute_script("arguments[0].click();",accept_btn)
    except:
        pass
    
    login_email=driver.find_element(by=By.NAME,value="current-email")
    login_password=driver.find_element(by=By.NAME,value="current-password")

    login_email.send_keys("username")
    login_password.send_keys("password")

    submit_button = driver.find_element(By.XPATH, "//button[contains(., 'sign')]")
    driver.execute_script("arguments[0].click();", submit_button)
    try:
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "message"))
        )
        if "incorrect" in error.text.lower():
            driver.quit()
            return -1
    except:
        pass

    # success
    return 1

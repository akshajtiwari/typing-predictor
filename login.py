from dotenv import load_dotenv
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions
import time
import os
options=webdriver.ChromeOptions()
options.add_experimental_option("prefs",{

    "download.default_directory":r"/home/akshajtiwari/Desktop/typing_predictor/downloaded_files", # linux style path
    "download.prompt_for_download":False,
    "download.directory_upgrade":True,
    "safebrowsing.enabled":True
    })
driver=webdriver.Chrome(options=options)

def login():
    load_dotenv()
    driver.get("https://monkeytype.com/login")
    wait = WebDriverWait(driver, 15)
    # click accept cookies
    try:
        accept_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'accept')]")))
        driver.execute_script("arguments[0].click();",accept_btn)
        
    except:
        pass
    
    # get email and password from the env
    login_email_btn=driver.find_element(by=By.NAME,value="current-email")
    login_password_btn=driver.find_element(by=By.NAME,value="current-password")

    get_username=os.getenv("username")
    get_password=os.getenv("password")

    login_email_btn.send_keys(get_username)
    time.sleep(2) # add a 2 second gap between adding email and password to bypass bot detection
    login_password_btn.send_keys(get_password)
    
    try:
        submit_button=driver.find_element(By.CLASS_NAME,"signIn")
        submit_button.click()
        try:
            WebDriverWait(driver, 20).until(
            EC.url_contains("/account")
        )
            print("login was sucessfull ( just login)")
            return True
            
        except:
            print("invalid credentials")
            return False
    except Exception as e:
        print("Login error:", e)
        return False

def download_csv():
    driver.get("https://monkeytype.com/account")
    driver.implicitly_wait(20.0)
    export_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Export CSV')]")
    if(export_btn.is_displayed()):
        print("export button found ")
        # export_btn.click()
        driver.execute_script("arguments[0].click();", export_btn)
        print("button was clicked successfully \n waiting for downloading the file")
        
        time.sleep(20) # wait for 20 seconds to let the download complete
        
        return True

    else:
        return False

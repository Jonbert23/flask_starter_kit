from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Global_xpath import LoginXpath
from flask import flash

class Login:
    @staticmethod
    def login(url):
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ERROR'}

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=d)
        driver.implicitly_wait(120)

        res = Login.openUrl(driver, url)

        if not res["success"]:
            flash(res["message"], category="error")
            driver.quit()
            return False


        username = LoginXpath.username
        password = LoginXpath.password
        loginbtn = LoginXpath.login_btn

        # landing page
        
        res = Login.authenticate(driver, username, password, loginbtn)
        
        if not res['success']:
            flash(res["message"], category="error")
            driver.quit()
            return False

        return driver

    @staticmethod
    def authenticate(driver, username, password, loginbtn):
        email = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, f"{username}"))
        )
        # email = driver.find_element(by=By.XPATH, value=f'{username}')
        email.send_keys("testryan")
        password = driver.find_element(by=By.XPATH, value=f'{password}')
        password.send_keys("Jarvis.123")
        loginbtn = driver.find_element(by=By.XPATH, value=f'{loginbtn}')

        loginbtn.click()

        try:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, LoginXpath.login_error))
            )
            return {
                "success": False,
                "message": "Invalid credentials."
            }
        except Exception as e:
            pass
        return{
            "success": True
        }

    @staticmethod
    def openUrl(driver, url):
        driver.get(url)
        
        try:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, LoginXpath.no_vpn))
            )
            if "Network Error" in element.text:
                return {
                    "success": False,
                    "message": "Not connected to the Jarvis Network."
                }
        except Exception as e:
            pass

        try:
            element = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, LoginXpath.logo_xpath))
            )
        except Exception as e:
            return {
                "success": False,
                "message": "Invalid Jarvis Analytics URL."
            }

        return {
            "success": True
        }

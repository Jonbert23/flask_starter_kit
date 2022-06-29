from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def netProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    driver.implicitly_wait(1000000000)
    moduleName = "Financials"
    netProdText = "Net Production"
    netProdValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/section[2]/div/div[2]/div/div/div[2]/h3").text
    
    financialNetProd = []
    financialNetProd = [moduleName, netProdText, netProdValue]
    

    return financialNetProd


def grossProduction(driver):
    driver.implicitly_wait(1000000000)
    moduleName = "Financials"
    grossProdText = "Gross Production"
    grossProdValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/section[2]/div/div[1]/div/div/div[2]/h3").text
   
    
    financialGrossProd = []
    financialGrossProd = [moduleName, grossProdText, grossProdValue]
    return financialGrossProd


def adjustment(driver):
    driver.implicitly_wait(1000000000)
    moduleName = "Financials"
    adjustmentText = "Adjustment Production"
    adjustmentValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/section[2]/div/div[3]/div/div/div[2]/h3").text
    

    financialAdjustment = []
    financialAdjustment = [moduleName, adjustmentText, adjustmentValue]
    return financialAdjustment

    
    
    
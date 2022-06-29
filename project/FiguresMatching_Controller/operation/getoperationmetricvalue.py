from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def netProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    driver.implicitly_wait(1000000000)
    moduleName = "Operation"
    netProdText = "Net Production"
    netProdValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[5]/span/span[1]").text
    
    operationNetProd = []
    operationNetProd = [moduleName, netProdText, netProdValue]
    

    return operationNetProd


def grossProduction(driver):
    driver.implicitly_wait(1000000000)
    moduleName = "Operation"
    grossProdText = "Gross Production"
    grossProdValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[2]/span/span[1]").text
    
    operationGrossProd = []
    operationGrossProd = [moduleName, grossProdText, grossProdValue]
    

    return operationGrossProd


def adjustment(driver):
    driver.implicitly_wait(1000000000)
    moduleName = "Operation"
    adjustmentText = "Adjustment"
    adjustmentValue = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div/div/div[2]/div/table/tbody/tr/td[3]/span/span[1]").text
    
    operationAdjustment = []
    operationAdjustment = [moduleName, adjustmentText, adjustmentValue]
    

    return operationAdjustment
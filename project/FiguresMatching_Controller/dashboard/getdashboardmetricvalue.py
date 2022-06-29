from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def netProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    driver.implicitly_wait(1000000000)
    moduleName = "Dashboard"
    netProdText = "Net Production"
    netProdValue = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/section/div[2]/div[2]/div/div/div[1]/div/h3").text
    
    dashboardNetProd = []
    dashboardNetProd = [moduleName, netProdText, netProdValue]
    

    return dashboardNetProd


def grossProduction(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    driver.implicitly_wait(1000000000)
    moduleName = "Dashboard"
    grossProdText = "Gross Production"
    grossProdValue = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/section/div[2]/div[1]/div/div/div[1]/div/h3").text
    
    dashboardGrossProd = []
    dashboardGrossProd = [moduleName, grossProdText, grossProdValue]
    

    return dashboardGrossProd


def adjustment(driver):
    # wait = WebDriverWait(driver, 120)
    # wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/h4')))
    driver.implicitly_wait(1000000000)
    moduleName = "Dashboard"
    adjustmentText = "Adjustment Production"
    adjustmentValue = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/section/div[2]/div[3]/div/div/div[1]/div/h3").text
    
    dashboardAdjustment = []
    dashboardAdjustment = [moduleName, adjustmentText, adjustmentValue]
    

    return dashboardAdjustment
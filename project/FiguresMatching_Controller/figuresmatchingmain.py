from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from project.FiguresMatching_Controller.financials import getfinancialsmetricvalue
from project.FiguresMatching_Controller.operation import getoperationmetricvalue
from project.FiguresMatching_Controller.dashboard import getdashboardmetricvalue
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(modules, metrics):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(1000000000) 
    driver.get('https://mb2.stage.jarvisanalytics.com/')
    allData = []
    

    usernameXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[1]/div/input')
    usernameXpath.send_keys('harristestadmin')
    passwordXpath = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/div[2]/div[2]/input')
    passwordXpath.send_keys('qa')
    loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[1]/div/form/button')
    loginButton.click()

    for x in modules:
        print("---"+x)
        if x == "Financials":
            driver.get('https://mb2.stage.jarvisanalytics.com/financial/summary')
            locationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div")
            locationFilter.click()
            lastMonthLocationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div/div[2]/div/div[1]/ul/li[7]")
            lastMonthLocationFilter.click()
            clickUpdateButton = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[3]")
            clickUpdateButton.click()
            for y in metrics:
                if y == "Net Production":
                    # LOCATION FILTER LAST MONTH
                    financialNetProdVal = getfinancialsmetricvalue.netProduction(driver)
                    allData.append(financialNetProdVal)
                    for financialNetProdVals in financialNetProdVal:
                        print("FINANCIAL NET OUTSIDE ARRAY: " + financialNetProdVals ) 
                if y == "Gross Production":
                    financialGrossProdVal = getfinancialsmetricvalue.grossProduction(driver)
                    allData.append(financialGrossProdVal)
                    for financialGrossProdVals in financialGrossProdVal:
                        print("FINANCIAL GROSS OUTSIDE ARRAY: " + financialGrossProdVals ) 
                if y == "Adjustment":
                    financialAdjustmentVal = getfinancialsmetricvalue.adjustment(driver)
                    allData.append(financialAdjustmentVal)
                    for financialAdjustmentVals in financialAdjustmentVal:
                        print("FINANCIAL GROSS OUTSIDE ARRAY: " + financialAdjustmentVals ) 
        if x == "Operations":
            driver.get('https://mb2.stage.jarvisanalytics.com/operations/offices')
            locationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div")
            locationFilter.click()
            lastMonthLocationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div/div[2]/div/div[1]/ul/li[7]")
            lastMonthLocationFilter.click()
            clickUpdateButton = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[4]")
            clickUpdateButton.click()
            for y in metrics:
                if y == "Net Production":
                    operationNetProdVal = getoperationmetricvalue.netProduction(driver)
                    allData.append(operationNetProdVal)
                    for operationNetProdVals in operationNetProdVal:
                        print("OPERATION NET PROD OUTSIDE ARRAY: " + operationNetProdVals )
                if y == "Gross Production":
                    operationGrossProdVal = getoperationmetricvalue.grossProduction(driver)
                    allData.append(operationGrossProdVal)
                    for operationGrossProdVals in operationGrossProdVal:
                        print("OPERATION GROSS PROD OUTSIDE ARRAY: " + operationGrossProdVals )
                if y == "Adjustment":
                    operationAdjustmentVal = getoperationmetricvalue.adjustment(driver)
                    allData.append(operationAdjustmentVal)
                    for operationAdjustmentVals in operationAdjustmentVal:
                        print("OPERATION ADJUSTMENT OUTSIDE ARRAY: " + operationAdjustmentVals )
        if x == "Dashboard":
            driver.get('https://mb2.stage.jarvisanalytics.com/dashboard')
            cancelAllLocation = driver.find_element(By.XPATH, "/html/body/div/main/div[1]/div/div/div/div[6]/button")
            cancelAllLocation.click()
            locationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div")
            locationFilter.click()
            locationLastMonthFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[1]/div/div[2]/div/div[1]/ul/li[7]")
            locationLastMonthFilter.click()
            locationFilter = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[2]/div")
            locationFilter.click()
            locationClear = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/div/span[3]")
            locationClear.click()
            selectLocationClear = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[2]/div/div/div[2]/div[2]/ul/li[1]")
            selectLocationClear.click()
            clickApplyButton = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[2]/div/div/div[3]/button[2]")
            clickApplyButton.click()
            clickUpdateButton = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[1]/div/div/div/div[6]/button")
            clickUpdateButton.click()   
            for y in metrics:
                if y == "Net Production":
                    dashboardNetProdVal = getdashboardmetricvalue.netProduction(driver)
                    allData.append(dashboardNetProdVal)
                    for dashboardNetProdVals in dashboardNetProdVal:
                        print("DASHBOARD NET PROD OUTSIDE ARRAY: " + dashboardNetProdVals )
                if y == "Gross Production":
                    dashboardGrossProdVal = getdashboardmetricvalue.grossProduction(driver)
                    allData.append(dashboardGrossProdVal)
                    for dashboardGrossProdVals in dashboardGrossProdVal:
                        print("DASHBOARD GROSS PROD OUTSIDE ARRAY: " + dashboardGrossProdVals )
                if y == "Adjustment":
                    dashboardAdjustmentVal = getdashboardmetricvalue.adjustment(driver)
                    allData.append(dashboardAdjustmentVal)
                    for dashboardAdjustmentVals in dashboardAdjustmentVal:
                        print("DASHBOARD NET PROD OUTSIDE ARRAY: " + dashboardAdjustmentVals )

    driver.quit()
    return allData
    # heyJude = "Let's Sing"
    # return heyJude


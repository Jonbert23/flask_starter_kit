from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from .Dashboard_xpath import BreakdownXpath, GlobalXpath, ProductionTest, ServiceTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Project.Controller.Global_Controller.Global_test import Login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Project.Controller.Global_Controller.Global_test import calendarDateRange

# --Blueprint
dash = Blueprint('dash', __name__)

@login_required
@dash.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        d = DesiredCapabilities.CHROME
        d['loggingPrefs'] = {'browser': 'ERROR'}
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=d)
        Login.login(driver, "https://solo.next.jarvisanalytics.com/solo/results", "testryan", "Jarvis.123")

        if not driver:
            return False

        date_from = "2022-06-01"
        date_to = "2022-06-30"
        test_result = automationTest(driver, date_from, date_to)
        print(test_result)

        return render_template('Dashboard_Template/Dashboard_index.html', test_result=test_result)

    return render_template('Dashboard_Template/Dashboard_index.html')


def automationTest(driver, date_from, date_to):
    #Calendar Date Range
    calendarDateRange(driver, date_from, date_to)

    # Update Button
    update_btn = WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, f"{GlobalXpath.update_btn}")))
    update_btn.click()

    # Testing
    breakdown_test = breakdownTest(driver)
    production_test = productionTest(driver)
    service_test = serviceTest(driver)

    time.sleep(5)
    allTest = [breakdown_test, production_test, service_test]

    return allTest

def getmetricsXpath(metrics, test):
    metric = {}
    if test == "brkTest":
        for x in metrics:
            metric[x] = BreakdownXpath.financial_dataxpath[x]

        return metric

    if test == "prodTest":
        print(test)
        for x in metrics:
            metric[x] = ProductionTest.production_testxpath[x]

        return metric

def breakdownTest(driver):
    metrics = ["net_prod", "gross_prod", "collection", "adjustment", "newpatient_visit", "existingpatient_visit"]
    metricsXpath = getmetricsXpath(metrics, "brkTest")
    values = {}

    if metrics:
        for metric in metricsXpath:
            values[metric] = []
            metric_base = metricsXpath[metric][0]
            metric_brk = metricsXpath[metric][1]
            metric_brktotal = metricsXpath[metric][2]
            metric_brkclose = metricsXpath[metric][3]

            values[metric].append(WebDriverWait(driver, 120).until(
                EC.visibility_of_element_located((By.XPATH, f"{metric_base}"))).text.replace('$ ','').replace('(', '-').replace(')',''))
            breakdownbtn = driver.find_element(by=By.XPATH, value=f'{metric_brk}')
            breakdownbtn.click()
            values[metric].append(WebDriverWait(driver, 120).until(
                EC.visibility_of_element_located((By.XPATH, f"{metric_brktotal}"))).text.replace('$ ','').replace('(', '-').replace(')',''))
            breakdownCloseBtn = driver.find_element(by=By.XPATH, value=f'{metric_brkclose}')
            breakdownCloseBtn.click()


            status = testValue(values[metric])
            values[metric].append(status)

    return values

def productionTest(driver):
    metrics = ["providers_data", "table_total", "payor_score"]
    metricsXpath = getmetricsXpath(metrics, "prodTest")
    values = {}

    if metrics:
        net_prod = WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, f"{ProductionTest.netprod_base}"))).text.replace('$ ','').replace('(', '-').replace(')','')

        for metric in metricsXpath:
            values[metric] = []
            metric_base = metricsXpath[metric][0]
            if metric != "payor_score":
                print("---not payor score")
                values[metric].append(WebDriverWait(driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH, f"{metric_base}"))).text.replace('$ ','').replace('(', '-').replace(')',''))
                values[metric].append(net_prod)
            else:
                print("---payor score")
                metric_view = WebDriverWait(driver, 120).until(
                        EC.visibility_of_element_located((By.XPATH, f"{GlobalXpath.metric_view}")))
                actions = ActionChains(driver)
                actions.move_to_element(metric_view).click().perform()

                values[metric].append(WebDriverWait(driver, 120).until(
                    EC.visibility_of_element_located((By.XPATH, f"{metric_base}"))).text.replace('$ ','').replace('(', '-').replace(')',''))
                values[metric].append(net_prod)

            status = testValue(values[metric])
            values[metric].append(status)

    return values

def testValue(values):
    if values[0] != values[1]:
        status = "Fail"

    if values[0] == values[1]:
        status = "Pass"

    return status

def serviceTest(driver):
    stopper = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section[4]/div/div[2]/div/div/table/tbody/tr[1]").text
    values={}
    service_code = driver.find_elements(By.XPATH, f"{ServiceTest.service_code}")
    for count, codes in enumerate(service_code):
        code = codes.text
        if count < 11:
           values[code] = []
        else:
            break

    for value_code in values:
        search_input = WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, f"{ServiceTest.search_input}"))
        )
        # Select all Search
        search_input.send_keys(Keys.CONTROL + "a")
        # Clear Search
        search_input.send_keys(Keys.DELETE)
        # Search Service Code
        search_input.send_keys(value_code)
        # Enter Search
        search_input.send_keys(Keys.ENTER)
        print(stopper)

        search_code = driver.find_elements(By.XPATH, f"{ServiceTest.service_code}")
        for codes in search_code:
            if code in values[code]:
                code = codes.text
                print(f"{code}")

    print(values)




from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from .Dashboard_xpath import BreakdownXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .Dashboard_tester import testDashboard
import time

# --Blueprint
dash = Blueprint('dash', __name__)

@login_required
@dash.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        driver = testDashboard("as")
        date_from = "2022-07-01"
        date_to = "2022-07-31"
        breakdownTest(driver, date_from, date_to)

    return render_template('Dashboard_Template/Dashboard_index.html')


def getmetricsXpath(metrics):
    metric = {}

    for x in metrics:
        metric[x] = BreakdownXpath.financial_dataxpath[x]

    return metric

# Select Date-Range in Calendar
def dateFrom():
    pass

def dateTo(date_to):
    yt, mt, dt = date_to.split('-')

def setdateCalendar(driver, date_from, date_to):
    yf, mf, df = date_from.split('-')

    print("----Calendar Date----")

    time.sleep(5)
    dateElement = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, f"{BreakdownXpath.date_picker}")))
    dateElement.click()

    month = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, f"{BreakdownXpath.curr_monthfrom}"))
    )
    date_month = month.text

    year = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, f"{BreakdownXpath.curr_yearfrom}"))
    )
    date_year = year.text

    print(date_month)
    print(date_year)


def breakdownTest(driver, date_from, date_to):
    setdateCalendar(driver, date_from, date_to)

    metrics = ["net_prod", "gross_prod", "collection", "adjustment", "newpatient_visit", "existingpatient_visit"]
    metricsXpath = getmetricsXpath(metrics)

    if metrics:
        for metric in metricsXpath:
            metric_base = metricsXpath[metric][0]
            metric_brk = metricsXpath[metric][1]
            metric_brktotal = metricsXpath[metric][2]
            metric_brkclose = metricsXpath[metric][3]

            print(f"------->{metric_base}")
            print(f">{metric_brk}")
            print(f">{metric_brktotal}")
            print(f">{metric_brkclose}")

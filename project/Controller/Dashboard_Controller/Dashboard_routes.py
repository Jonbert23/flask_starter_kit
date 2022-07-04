from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from .Dashboard_xpath import BreakdownXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dash = Blueprint('dash', __name__)

@login_required
@dash.route("/dashboard", methods=['POST', 'GET'])
def dashboard():
    if request.method == 'POST':
        url = "https://solo.next.jarvisanalytics.com/solo/results"
        date_from = "2022-07-01"
        date_to = "2022-07-31"
        breakdownTest(date_from, date_to)

    return render_template('Dashboard_Template/Dashboard_index.html')


def getmetricsXpath(metrics):
    metric = {}

    for x in metrics:
        metric[x] = BreakdownXpath.financial_dataxpath[x]

    return metric



def breakdownTest(date_from, date_to):

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

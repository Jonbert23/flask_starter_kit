from Project.Controller.Global_Controller.Global_test import Login
from .Eod_xpath import EodXpath, BreakdownXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def testEod(testcode):
    # INSERT CODE FOR DECODING THE TESTCODE

    driver = Login.login("https://solo.next.jarvisanalytics.com/end-of-day")

    if not driver:
        return False
    try:
        xpaths = getXpath()

        result = {}
        for metric in xpaths:
            # print(xpaths[metric]["main"])

            result[metric]["main"] = driver.find_element(
                by = By.XPATH,
                value = xpaths[metric]["main"]
            ).text
        
        print(result)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def getXpath():
    return {
        "collection": getMainBreakdown(EodXpath.collection, BreakdownXpath.collection),
        "adjustments": getMainBreakdown(EodXpath.adjustments, BreakdownXpath.adjustments),
        "case_acceptance": getMainBreakdown(EodXpath.case_acceptance, BreakdownXpath.case_acceptance),
        "missing_ref": getMainBreakdown(EodXpath.missing_ref, BreakdownXpath.missing_ref),
        "no_show": getMainBreakdown(EodXpath.no_show, BreakdownXpath.no_show),
        "daily_coll": getMainBreakdown(EodXpath.daily_coll, BreakdownXpath.daily_coll),
        "hyg_reapp": getMainBreakdown(EodXpath.hyg_reapp, BreakdownXpath.hyg_reapp),
        "new_patients": getMainBreakdown(EodXpath.new_patients, BreakdownXpath.new_patients),
        "same_day_treat": getMainBreakdown(EodXpath.same_day_treat, BreakdownXpath.same_day_treat),
        "pt_portion": getMainBreakdown(EodXpath.pt_portion, BreakdownXpath.pt_portion)
    }

def getMainBreakdown(main, breakdown):
    return {
        "main": main,
        "breakdown": breakdown
    }
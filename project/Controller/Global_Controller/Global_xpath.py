class LoginXpath:
    username = '/html/body/div/div/div/div/div[1]/div/form/div[1]/div/input'
    password = '/html/body/div/div/div/div/div[1]/div/form/div[2]/div[2]/input'
    login_btn = '/html/body/div/div/div/div/div[1]/div/form/button'
    login_error = '/html/body/div/div/div/div/div[1]/div/form/p'
    logo_xpath = '/html/body/div/div/div/div/div[1]/div/div/a/img'
    no_vpn = '/html/body/div/div/div[1]'

class EodXpath:
    collection = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[13]/div[2]/input'
    adjustments = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[12]/div[2]/input'
    case_acceptance = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[20]/div[2]/input'
    missing_ref = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[24]/div[2]/input'
    no_show = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[17]/div[2]/input'
    daily_coll = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[14]/div[2]/input'
    hyg_reapp = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[28]/div[2]/input'
    new_patients = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[21]/div[2]/input'
    same_day_treat = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[18]/div[2]/input'
    pt_portion = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[5]/div[2]/input'

class EodBreakdownXpath:
    collection = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[13]/div[1]/div/span/a'
    adjustments = '/html/body/div[1]/main/div[2]/div[3]/div[1]/div/form/div/div[1]/div[1]/div/div[12]/div[1]/div/span/a'

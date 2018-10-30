import yaml
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_driver():

    with open(PATH('../config/desired_caps.yaml'), 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': '8.0',
        'deviceName': '4a7e9ca6',
        'noReset': data['noReset'],
        'appActivity': data['appActivity'],
        'appPackage': data['appPackage'],
        'automationName': data['automationName'],
        'recreateChromeDriverSessions': True
    }

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    return driver

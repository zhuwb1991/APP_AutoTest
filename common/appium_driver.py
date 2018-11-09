import yaml
import os
from appium import webdriver
import unittest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_driver(info):
    with open(PATH('../config/desired_caps.yaml'), 'r', encoding='utf-8') as f:
        data = yaml.load(f)

    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': info['release'],
        'deviceName': info['deviceName'],
        'noReset': data['noReset'],
        'appActivity': data['appActivity'],
        'appPackage': data['appPackage'],
        'resetKeyboard': data['resetKeyboard'],
        'unicodeKeyboard': data['unicodeKeyboard'],
        'automationName': data['automationName'],
        'recreateChromeDriverSessions': True
    }

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(info['port']) + '/wd/hub', desired_caps)
    return driver


class ParametrizedTestCase(unittest.TestCase):

    def __init__(self, methodName="runTest", param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global device
        device = param

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_driver(device)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()
        cls.driver.quit()

    @staticmethod
    def param_test(test_class, param=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(test_class)

        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(test_class(name, param=param))
        return suite

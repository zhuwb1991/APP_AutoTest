from common.utils import get_yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


def get_locators(page_name, element_name):

    locators = get_yaml(PATH("../businessPage/pages.yaml"))[page_name]['locators']

    for l in locators:
        if l['desc'] == element_name:
            return l


class LoginPage: 
    account = get_locators('LoginPage', '账号')
    passwd = get_locators('LoginPage', '密码')
    login_btn = get_locators('LoginPage', '登录按钮')


class LaunchPage: 
    start_btn = get_locators('LaunchPage', '开始使用')


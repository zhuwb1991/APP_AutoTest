from common.utils import get_yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


def get_locators(page_name, element_name):

    locators = get_yaml(PATH("../businessPage/pages.yaml"))[page_name]['locators']

    for l in locators:
        if l['name'] == element_name:
            return l


class LaunchPage:
    """
    启动页元素
    """
    start_btn = get_locators('LaunchPage', '开始使用')


class LoginPage:
    """
    登录页元素
    """
    account = get_locators('LoginPage', '账号')
    passwd = get_locators('LoginPage', '密码')
    login_btn = get_locators('LoginPage', '登录')


if __name__ == '__main__':
    print(LoginPage.passwd)

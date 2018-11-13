import unittest
from common.appium_driver import ParametrizedTestCase
from common.common_fun import Common
from businessPage.pages import LaunchPage, LoginPage
import time


class LoginTest(ParametrizedTestCase):

    # def test01_nologin(self):
    #     l = LoginPage(self.driver)
    #
    #     # 启动APP
    #     time.sleep(5)
    #     l.permission_btn()
    #     l.swipe_left()
    #     time.sleep(1)
    #     l.swipe_left()
    #     l.click(l.start_btn)

    def test02_login(self):

        # 启动APP
        time.sleep(3)
        COM.permission_btn()
        COM.swipe_left()
        COM.swipe_left()
        COM.click(LaunchPage.start_btn)

        # 登录操作
        COM.send_keys(LoginPage.account, 'xxxxxx')
        COM.send_keys(LoginPage.passwd, 'xxxxxx')
        COM.click(LoginPage.login_btn)
        time.sleep(6)
        COM.permission_btn()

        # 关闭发票弹窗
        # c.click(c.cancel_btn)
        time.sleep(5)

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        global COM
        COM = Common(cls.driver)


if __name__ == '__main__':
    unittest.main()

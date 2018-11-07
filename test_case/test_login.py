import unittest
from common.base_case import TestCase
from businessPage.loginPage import LoginPage
import time


class LoginTest(TestCase):

    def test_login(self):
        l = LoginPage(self.driver)
        time.sleep(5)
        l.swipe_left()
        time.sleep(1)
        l.swipe_left()
        l.click(l.start_btn)

        l.passwd_login('zwbapi5@yopmail.com', 'qqqqqq')
        time.sleep(10)

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()


if __name__ == '__main__':
    unittest.main()

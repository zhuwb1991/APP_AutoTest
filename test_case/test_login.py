import unittest
from common.base_case import TestCase
from businessPage.loginPage import LoginPage


class LoginTest(TestCase):

    def test_login(self):

        l = LoginPage(self.driver)


        # username = "zhu"
        l.login_action()

        l.check_point()


if __name__ == '__main__':
    unittest.main()

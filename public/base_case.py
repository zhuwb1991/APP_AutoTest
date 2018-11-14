import unittest
from public.appium_driver import appium_driver


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def tearDown(self):
        pass

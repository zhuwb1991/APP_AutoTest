import unittest
from common.desired_caps import appium_desired


class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_desired()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def tearDown(self):
        pass

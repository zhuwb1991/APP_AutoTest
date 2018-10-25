from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException

WAIT_TIME = 30


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def finds_element(self, *loc):
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(expected_conditions.presence_of_element_located(loc))
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            print("元素不存在")
        except TimeoutException:
            print("超时")
        except WebDriverException:
            print("driver出问题了")

    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located(*loc))
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            print("元素不存在")
        except TimeoutException:
            print("超时")
        except WebDriverException:
            print("driver出问题了")

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
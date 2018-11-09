from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, WebDriverException
from common.logs import Log


log = Log()
WAIT_TIME = 30


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, WAIT_TIME).until(lambda x: self.find_by(loc))
            return self.find_by(loc)
        except NoSuchElementException:
            print("元素不存在")
            log.info("元素" + loc['name'] + '不存在')
        except TimeoutException:
            print("超时")
            log.info("查找" + loc['name'] + "超时")
        except WebDriverException:
            print("driver出问题了")

    def find_by(self, loc):
        """
        封装元素查找方法
        :param loc: 操作元素的字典
        :return:
        """
        elements = {
            "id": lambda: self.driver.find_element_by_id(loc["value"]),
            "ids": lambda: self.driver.find_elements_by_id(loc["value"]),
            "class_name": lambda: self.driver.find_element_by_class_name(loc["value"]),
            # "ui": lambda: self.driver.find_element_by_android_uiautomator
            # ('new UiSelector().text("%s")' % loc["uiText"]),
            "xpath": lambda: self.driver.find_element_by_xpath(loc["value"]),
            "content-desc": lambda: self.driver.find_element_by_accessibility_id(loc["value"])
        }
        return elements[loc["type"]]()

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
from basePage.basePage import BasePage
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By


class Common(BasePage):

    def get_screen_size(self):
        """
         获取屏幕尺寸
        :return: 
        """
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipe_left(self):
        """
        左滑屏幕
        :return:
        """
        l = self.get_screen_size()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.75)
        x2 = int(l[0] * 0.05)
        self.swipe(x1, y1, x2, y1, 600)

    def swipe_up(self):
        """
        上滑屏幕
        :return:
        """
        l = self.get_screen_size()
        self.driver.swipe(l[0]/2, l[1]*3/4, l[0]/2, l[1]/4)

    def swipe_to_show(self, element):
        """
        判断元素是否在当前页面，无则滑动屏幕查找
        :param element: 传入元素的id或text属性
        :return:
        """
        for i in range(1, 5):
            if not element in self.driver.page_source:
                l = self.get_screen_size()
                self.driver.swipe(l[0]/2, l[1]*3/4, l[0]/2, l[1]/2)
            break

    def get_activity(self):
        """
        获取当前页面activity
        :return:
        """
        return self.driver.current_activity

    def permission_btn(self):
        """
        处理权限弹窗
        """
        button1 = "总是允许"
        button2 = "始终允许"
        button3 = "允许该操作"
        button4 = "允许"
        list_btn = [button1, button2, button3, button4]
        for btn in list_btn:
            if btn in self.driver.page_source:
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + btn + '")').click()
                break


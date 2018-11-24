import time
from .base_page import BasePage
from appium.common.exceptions import NoSuchContextException
from appium.webdriver.common.touch_action import TouchAction


class Common(BasePage):

    def click(self, loc, index=0):
        """
        点击操作
        :param loc:
        :param index: 一组元素时的index值
        :return:
        """
        if index != 0:
            self.find_element(loc)[index].click()
        else:
            self.find_element(loc).click()

    def send_keys(self, loc, value, index=0):
        """
        输入操作
        :param loc:
        :param value:
        :param index: 一组元素时的index值
        :return:
        """
        if index != 0:
            self.find_element(loc)[index].clear()
            self.find_element(loc)[index].send_keys(value)
        else:
            self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)

    def press_keycode(self, code):
        """
        模拟点击系统按键
        :param code:
        :return:
        """
        self.driver.press_keycode(code)

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
        time.sleep(1)

    def swipe_up(self):
        """
        上滑屏幕
        :return:
        """
        l = self.get_screen_size()
        self.driver.swipe(l[0]/2, l[1]*3/4, l[0]/2, l[1]/4)
        time.sleep(1)

    def switch_webview(self):
        try:
            n = 1
            while n < 10:
                time.sleep(3)
                n = n + 1
                print(self.driver.contexts)
                for cons in self.driver.contexts:
                    if cons.lower().startswith("webview"):
                        self.driver.switch_to.context(cons)
                        self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                        self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
                        return {"result": True}
            return {"result": False}
        except NoSuchContextException:
            # log.error("切换webview失败")
            pass

    def switch_native(self):
        self.driver.switch_to.context("NATIVE_APP")

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

    def long_press(self, loc, index=0):
        """
        长按操作
        :return:
        """
        if index != 0:
            self.touch_action().long_press(self.find_element(loc)[index], duration=1800).perform()
            return {"result": True}
        else:
            self.touch_action().long_press(self.find_element(loc), duration=1800).perform()

    def touch_action(self):
        return TouchAction(self.driver)

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
                try:
                    self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + btn + '")').click()
                    break
                except:
                    pass


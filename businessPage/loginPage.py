import time
from common.common_fun import Common, By


class LoginPage(Common):

    # 登录界面元素
    username_text = (By.ID, 'xxx')

    def login_action(self):

        # self.swipe_left()
        # self.swipe_left()
        # time.sleep(5)
        self.finds_element(*self.username_text).click()
        time.sleep(5)

    def check_point(self):
        pass

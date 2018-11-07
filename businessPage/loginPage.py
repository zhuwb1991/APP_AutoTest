from common.common_fun import Common, By


class LoginPage(Common):

    # 启动界面
    start_btn = (By.ID, 'com..BizCardReader:id/launch_guide_uesr_now')

    # 账号密码登陆界面
    account = (By.ID, 'com..BizCardReader:id/login_email')
    password = (By.ID, 'com..BizCardReader:id/login_pwd')
    login_btn = (By.ID, 'com..BizCardReader:id/login_btn')

    def passwd_login(self, account, password):
        self.send_keys(self.account, account)
        self.send_keys(self.password, password)
        self.click(self.login_btn)

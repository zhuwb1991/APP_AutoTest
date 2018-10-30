import yaml
import random
import time
import platform
import os
from common.logs import Log

log = Log()

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AppiumServer:
    def __init__(self, device):
        self.device = device

    def __start_driver(self, aport, bpport):
        """
        清理logcat与appium所有进程
        :return:
        """
        if platform.system() == 'Windows':
            import subprocess
            subprocess.Popen("appium -p %s -bp %s -U %s" %
                             (aport, bpport, self.device), shell=True)

    def start_appium(self, aport='4723'):
        """
        启动appium
        p:appium port
        bp:bootstrap port
        :return: 返回appium端口参数
        """
        # aport = random.randint(4700, 4900)
        bpport = random.randint(4700, 4900)
        self.__start_driver(aport, bpport)

        log.info(
            'start appium :p %s bp %s device:%s' %
            (aport, bpport, self.device))
        time.sleep(10)

    def main(self):
        """
        :return: 启动appium
        """
        return self.start_appium()

    def stop_appium(self):
        """
        停止appium
        :return:
        """
        if platform.system() == 'Windows':
            os.popen("taskkill /f /im node.exe")


if __name__ == '__main__':
    s = AppiumServer("915eaa74")
    s.main()

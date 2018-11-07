import unittest
import os
import time
import common.HTMLTestRunner
from common.appium_server import AppiumServer
import common.adb_tool as a
from common.adb_tool import ADB

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

test_dir = './test_case'
report_dir = './report'


def run_case():

    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    now = time.strftime("%Y%m%d%H%M")
    report_name = report_dir + '/' + now + '.html'

    fp = open(report_name, "wb")
    runner = common.HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="测试报告",
        description="测试结果"
    )
    runner.run(discover)
    fp.close()


if __name__ == '__main__':
    devices = a.get_devices()
    adb = ADB()
    if len(devices) > 0:
        for d in devices:
            # server = AppiumServer(d)
            # server.main()

            adb.clear_package('com..BizCardReader')

            run_case()
            # server.stop_appium()
    else:
        print("暂无连接的设备")

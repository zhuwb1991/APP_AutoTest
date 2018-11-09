import unittest
import os
import time
import common.HTMLTestRunner
from common.appium_server import AppiumServer
import common.adb_tool as a
from common.adb_tool import ADB
from common.appium_driver import ParametrizedTestCase
from test_case.test_login import LoginTest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

test_dir = './test_case'
report_dir = './report'


def run_case(device):

    # 加载测试用例
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.param_test(LoginTest, param=device))

    unittest.TextTestRunner(verbosity=2).run(suite)

    # now = time.strftime("%Y%m%d%H%M")
    # report_name = report_dir + '/' + now + '.html'
    #
    # fp = open(report_name, "wb")
    # runner = common.HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title="测试报告",
    #     description="测试结果"
    # )
    # runner.run(suite)
    # fp.close()


if __name__ == '__main__':
    devices = a.get_devices()

    if len(devices) > 0:
        for d in devices:
            adb = ADB(d)

            server = AppiumServer(d)
            device_info = adb.get_phone_info()

            info = {}

            # info["port"] = server.main()

            info["port"] = 4723
            info["deviceName"] = device_info["brand"]
            info["release"] = device_info["release"]

            adb.clear_package('com.xxx.BizCardReader')

            run_case(info)

            # server.stop_appium()
    else:
        print("暂无连接的设备")

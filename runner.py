import unittest
import threading
import os
import time
import public.HTMLTestRunner
from config.basic_config import performance_path
from performance.performance_data import GetData
from performance.performance_report import create_performance_report
from public.appium_server import AppiumServer
import public.adb_tool as a
from public.utils import get_yaml
from public.adb_tool import ADB
from public.appium_driver import ParametrizedTestCase
from test_case.test_login import LoginTest
from test_case.test_cards import CardTest
from test_case.test_group import GroupTest
from test_case.test_map import MapTest
from test_case.test_manage import ManageTest
from test_case.test_more_menu import MoreMenuTest
from test_case.test_group_chat import GroupChatTest

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

report_dir = './report'
package_name = get_yaml(PATH('./config/desired_caps.yaml'))['appPackage']


def run_case(device):

    # 加载测试用例
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.param_test(LoginTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(CardTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(GroupTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(MapTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(ManageTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(MoreMenuTest, param=device))
    suite.addTest(ParametrizedTestCase.param_test(GroupChatTest, param=device))

    # unittest.TextTestRunner(verbosity=2).run(suite)

    now = time.strftime("%Y%m%d%H%M")
    report_name = report_dir + '/' + now + '.html'

    fp = open(report_name, "wb")
    runner = public.HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="测试报告",
        description="测试结果"
    )
    runner.run(suite)
    fp.close()


def perform(device_id, version):

    while True:
        try:
            GetData(device_id, ADB(device_id).get_activity(version), package_name).get_mem()
            GetData(device_id, ADB(device_id).get_activity(version), 'com.xxx.Biz').get_cpu()
            GetData(device_id, ADB(device_id).get_activity(version), package_name).get_fps()
            time.sleep(2)
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    devices = a.get_devices()

    if len(devices) > 0:
        for d in devices:
            adb = ADB(d)

            server = AppiumServer(d)
            device_info = adb.get_phone_info()

            info = {}
            info["port"] = server.main()
            # info["port"] = 4723
            info["deviceName"] = device_info["brand"]
            info["release"] = device_info["release"]

            adb.clear_package(package_name)

            # 启动一个子线程，监测性能数据
            p = threading.Thread(target=perform, args=(d, device_info["release"]))
            p.setDaemon(True)
            p.start()

            run_case(info)
            server.stop_appium()
            create_performance_report(package_name, performance_path)
    else:
        print("暂无连接的设备")

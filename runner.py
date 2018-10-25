import unittest
import os
import time
import common.HTMLTestRunner

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

test_dir = './test_case'
report_dir = './report'


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

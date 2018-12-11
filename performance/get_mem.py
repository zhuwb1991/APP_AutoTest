import time
import os
from public.adb_tool import call_adb
from public.utils import write_file

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class GetMemory:

    def __init__(self, device_id, activity, package_name):
        self.device_id = device_id
        self.activity = activity
        self.package_name = package_name

    def get_mem(self):

        mem = '0'
        try:
            cmd = "adb -s {} shell dumpsys meminfo {}".format(self.device_id, self.package_name)
            result = call_adb(cmd)
            for line in result:
                if line.startswith(b"        TOTAL"):
                    mem = float(line.split()[1])/1024
                    # 保留两位小数
                    mem = format(mem, '.2f')
        except Exception as e:
            print(e)
        finally:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            info = current_time + '\t' + str(mem) + 'MB\t' + self.activity + '\n'
            write_file(PATH("../report/memory.txt"), info)

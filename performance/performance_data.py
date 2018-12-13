import time
import os
import subprocess
import re
from wsgiref.validate import validator
from public.adb_tool import call_adb
from public.utils import write_file

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class GetData:

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
            write_file(PATH("../report/performance/memory.txt"), info)

    def __get_cpu_kel(self):
        """
        查看CPU核数
        :return:
        """
        cmd = "adb -s {} shell cat /proc/cpuinfo".format(self.device_id)
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
        result = result.split()
        kel_num = re.findall("processor", str(result))
        return len(kel_num)

    def get_cpu(self):
        cpu = 0
        cpu_num = self.__get_cpu_kel()
        try:
            cmd = 'adb -s {} shell top -n 1 | find "{}"'.format(self.device_id, self.package_name)
            result = call_adb(cmd)
            temp = result[0]
            if temp:
                cpu = temp.decode().split()[-4]
                cpu = format(float(cpu)/cpu_num, '.2f')
        except Exception as e:
            print(e)
        finally:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            info = current_time + '\t' + str(cpu) + '\t' + self.activity + '\n'
            write_file(PATH("../report/performance/cpu.txt"), info)

    def get_fps(self):

        fps = 0
        try:
            cmd = "adb -s %s shell dumpsys gfxinfo %s" % (self.device_id, self.package_name)
            result = os.popen(cmd).read().strip()
            frames = [x for x in result.split('\n') if validator(x)]
            frame_count = len(frames)
            jank_count = 0
            vsync_overtime = 0
            render_time = 0
            for frame in frames:
                time_block = re.split(r'\s+', frame.strip())
                if len(time_block) == 4:
                    try:
                        render_time = float(time_block[0]) + float(time_block[1]) + float(time_block[2])
                    except Exception as e:
                        render_time = 0
                if render_time > 16.67:
                    jank_count += 1
                    if render_time % 16.67 == 0:
                        vsync_overtime += int(render_time / 16.67) - 1
                    else:
                        vsync_overtime += int(render_time / 16.67)
            fps = int(frame_count * 60 / (frame_count + vsync_overtime))
        except Exception as e:
            print(e)
        finally:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            info = current_time + '\t' + str(fps) + '\t' + self.activity + '\n'
            write_file(PATH("../report/performance/fps.txt"), info)


if __name__ == '__main__':
    G = GetData("98895a374351554653", 'main', 'com.intsig.Biz')
    print(G.get_fps())

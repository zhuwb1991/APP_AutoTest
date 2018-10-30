import subprocess
import time
import random


def call_adb(command):
    """
    调用cmd，执行命令，返回结果
    :param command:
    :return:
    """
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()


def get_devices():
    """
    获取设备
    :return:
    """
    devices = []
    command = "adb devices"
    for item in call_adb(command):
        t = item.decode().split("\tdevice")
        if (len(t)) >= 2:
            devices.append(t[0])
    return devices


class ADB:

    def __init__(self, device_id=""):
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "adb %s %s" % (self.device_id, str(args))
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def shell(self, args):
        cmd = "adb %s shell %s" % (self.device_id, str(args),)
        return subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

    def get_phone_info(self):
        """
        获取设备信息：设备名，系统版本
        :return:
        """
        phone_info = self.adb("shell cat /system/build.prop").stdout.readlines()
        result = {"release": "8.0", "brand": "HUAWEI", "device_name": "device1"}
        release = "ro.build.version.release="
        brand = "ro.product.brand="
        device_name = "ro.product.device="
        for line in phone_info:
            for i in line.split():
                item = i.decode()
                if item.find(release) >= 0:
                    result["release"] = item[len(release):]
                    break
                if item.find(brand) >= 0:
                    result["brand"] = item[len(brand):]
                    break
                if item.find(device_name) >= 0:
                    result["device_name"] = item[len(device_name):]
                    break
        print(result)
        return result

    def install_app(self, app_path):
        return self.adb("install -r %s" % app_path).stdout.readlines()

    def touch_by_element(self, element):
        """
        点击元素
        """
        self.shell("input tap %s %s" % (str(element[0]), str(element[1])))
        time.sleep(0.5)

    def get_focused_package_xml(self, save_path):
        # file_name = random.randint(10, 99)
        self.shell(
            'uiautomator dump /data/local/tmp/dump.xml').communicate()
        self.adb('pull /data/local/tmp/dump.xml {}'.format(save_path)).communicate()

    def is_install(self, package_name):
        """
        判断应用是否安装，已安装返回True，否则返回False
        usage: isInstall("com.example.apidemo")
        """
        if self.get_matching_app_list(package_name):
            return True
        else:
            return False

    def get_matching_app_list(self, keyword):
        """
        模糊查询与keyword匹配的应用包名列表
        usage: getMatchingAppList("qq")
        """
        # for packages in self.shell("pm list packages %s" % keyword).stdout.readlines():
        #     matApp.append(packages.split(":")[-1].splitlines()[0])
        return self.shell("pm list packages %s" % keyword).stdout.readlines()

    def clear_package(self, package_name):
        """
        清除缓存
        :return:
        """
        self.adb('shell pm clear %s' % package_name)


if __name__ == "__main__":
    A = ADB()
    A.get_phone_info()

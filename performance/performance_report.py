import os
import jinja2


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def read_performance_data(package_name, path):
    """
    读取性能数据
    :param package_name: 应用包名，过滤非当前包的数据
    :param path: 性能数据地址
    :return:
    """
    time = []
    info = []
    activity = []
    with open(path, 'r') as f:
        for index in f.readlines():
            # 过滤掉不是应用界面的数据
            if package_name in index.split('\t')[2].replace('\n', ''):
                time.append(index.split('\t')[0].replace('\n', ''))
                info.append(index.split('\t')[1].replace('\n', ''))
                activity.append(index.split('\t')[2].replace('\n', ''))
    return time, info, activity


def get_cpu_data(data):
    """
    传入读取的cpu数据，生成特定格式
    :param data:
    :return:
    """
    tuples = ()
    i = []
    j = []
    try:
        for index in range(len(data[0])):
            i.append(data[0][index])
            i.append(float(data[1][index]))
            j.append(i)
            i = []
    except Exception as e:
        print(e)
    tuples = tuples + tuple(j)
    return tuples


def get_memory_data(data):
    """
    传入读取的内存数据，生成特定格式
    :param data:
    :return:
    """
    tuples = ()
    i = []
    j = []
    try:
        for index in range(len(data[0])):
            i.append(data[0][index])
            i.append(float(data[1][index][:-2]))
            j.append(i)
            i = []

    except Exception as e:
        print(e)
    tuples = tuples + tuple(j)
    return tuples


def get_fps_data(data):
    """
    传入读取的fps数据，生成特定格式
    :param data:
    :return:
    """
    tuples = ()
    i = []
    j = []
    try:
        for index in range(len(data[0])):
            i.append(data[0][index])
            i.append(float(data[1][index]))
            j.append(i)
            i = []
    except Exception as e:
        print(e)
    tuples = tuples + tuple(j)
    return tuples


def create_performance_report(package_name, report_path):

    template_loader = jinja2.FileSystemLoader(searchpath=PATH("./"))
    template_env = jinja2.Environment(loader=template_loader)

    memory_data = read_performance_data(package_name, PATH("../report/performance/memory.txt"))
    memory_tuple = get_memory_data(memory_data)

    cpu_data = read_performance_data(package_name, PATH("../report/performance/cpu.txt"))
    cpu_tuple = get_cpu_data(cpu_data)

    fps_data = read_performance_data(package_name, PATH("../report/performance/fps.txt"))
    fps_tuple = get_fps_data(fps_data)

    template = template_env.get_template("report_template.html")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(template.render(appname='名片全能王',
                                data=memory_tuple, memtime=memory_data[0], meminfo=memory_data[1], memactivity=memory_data[2],
                                data1=cpu_tuple, cputime=cpu_data[0], cpuinfo=cpu_data[1], cpuactivity=cpu_data[2],
                                data3=fps_tuple, fpstime=fps_data[0], fpsinfo=fps_data[1], fpsactivity=fps_data[2],
                                ))


if __name__ == '__main__':
    create_performance_report("com.intsig.BizCardReader", r"C:\Users\wenbo_zhu\Desktop\app\test.html")
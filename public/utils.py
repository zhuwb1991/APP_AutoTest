import yaml


def get_yaml(path):
    try:
        with open(path, encoding="utf8") as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print("未找到文件:" + path)


def write_file(filename, content, cover=False):

    try:
        newstr = ''
        if isinstance(content, list or tuple):
            for item in content:
                newstr = newstr + item + '\n'
        else:
            newstr = content
        if cover:
            # 覆盖文件内容
            mode = 'w'
        else:
            mode = 'a'
        with open(filename, mode) as f:
            f.write(newstr)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    import os
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    result = get_yaml(PATH("../Yaml/demo.yaml"))
    print(result)

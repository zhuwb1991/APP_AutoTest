import yaml


def get_yaml(path):
    try:
        with open(path, encoding="utf8") as f:
            x = yaml.load(f)
            return x
    except FileNotFoundError:
        print("未找到文件:" + path)


if __name__ == "__main__":
    import os
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    result = get_yaml(PATH("../Yaml/demo.yaml"))
    print(result)

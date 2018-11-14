import jinja2
from public.utils import get_yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


def get_locators():
    """
    获取所有yaml页面，生成为一个页面元素字典
    :return:
    """
    yaml_page = {}

    for fpath, dirname, fnames in os.walk(PATH("../business_page/element")):

        for name in fnames:
            path = os.path.join(fpath, name)
            page = get_yaml(path)
            yaml_page.update(page)

    return yaml_page


def get_po(yaml_page):
    """
    从locators中得到desc和name,重新生成一个对象
    :param yaml_page:
    :return:
    """
    page_obj = {}

    for page, name in yaml_page.items():
        locs_names = {}
        locs = name['locators']

        for loc in locs:
            locs_names[loc['desc']] = loc['name']

        page_obj[page] = locs_names
    return page_obj


def create_page(page_list):
    """
    根据jinja2模板创建pages.py文件
    :param page_list:
    :return:
    """
    path = PATH('./')
    template_loader = jinja2.FileSystemLoader(searchpath=path)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
        'page_list': page_list
    }

    template = template_env.get_template("template")
    with open(PATH('./pages.py'), 'w', encoding='utf-8') as f:
        f.write(template.render(templateVars))


if __name__ == '__main__':
    yaml1 = get_locators()
    po = get_po(yaml1)
    create_page(po)

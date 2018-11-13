import jinja2
from common.utils import get_yaml
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


def get_locators():

    locators = get_yaml(PATH("../businessPage/pages.yaml"))
    return locators


def get_po(yaml_page):
    page_obj = {}

    for page, name in yaml_page.items():
        locs_names = {}
        locs = name['locators']

        for loc in locs:
            locs_names[loc['desc']] = loc['name']

        page_obj[page] = locs_names
    return page_obj


def create_page(page_list):

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

from business_page import tools
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


pages = tools.get_locators()


def get_locators(page_name, element_name):

    locators = pages[page_name]['locators']

    for l in locators:
        if l['desc'] == element_name:
            return l


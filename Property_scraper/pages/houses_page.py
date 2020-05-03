import re

from bs4 import BeautifulSoup

from locators.houses_page_locators import HousesPageLocators
from parsers.house import HouseParser


class HousesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def houses(self):
        return [HouseParser(e) for e in self.soup.select(HousesPageLocators.HOUSE)]

'''
    @property
    def page_count(self):
        locator = self.soup.select_one(HousesPageLocators.PAGER).string
        expression = "Page [0-9]+ of ([0-9]+)"
        matcher = re.match(expression, locator)
        pages = int(matcher.group(1))
        return pages
'''
import re

from locators.house_locators import HouseLocators


class HouseParser:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Vivienda de {self.bedrooms}, {self.bathrooms} y {self.surface} por un precio de {self.price}>'


    @property
    def price(self):
        locator = HouseLocators.PRICE
        currency = HouseLocators.CURRENCY
        if self.parent.select_one(currency).string != "UF":
            return self.parent.select_one(locator).string
        else:
            exchange = (int(self.parent.select_one(locator).string))*28000
            ex_formatted = f'{exchange:,d}'.replace(",", ".")
            return ex_formatted

    @property
    def surface(self):
        locator = HouseLocators.INFO
        info = self.parent.select_one(locator).string.split(" | ")
        return info[0]

    @property
    def bedrooms(self):
        locator = HouseLocators.INFO
        info = self.parent.select_one(locator).string.split(" | ")
        return info[1]

    @property
    def bathrooms(self):
        locator = HouseLocators.INFO
        info = self.parent.select_one(locator).string.split(" | ")
        return info[2]

'''
    @property
    def rating(self):
        locator = BookLocators.RATING
        classes = self.parent.select_one(locator).attrs["class"]
        rating_classes = [c for c in classes if c != "star-rating"]
        return BookParser.RATINGS.get(rating_classes[0])
'''
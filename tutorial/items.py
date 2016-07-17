# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CoopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = srapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
    is_organic = scrapy.Field()
    origin = scrapy.Field()

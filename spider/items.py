# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CategoryItem(scrapy.Item):
    category = scrapy.Field()
    url = scrapy.Field()
    number = scrapy.Field()


class BookItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

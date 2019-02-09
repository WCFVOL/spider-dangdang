import scrapy
from scrapy.loader import ItemLoader
from spider.items import BookItem
from spider.util import url_is_legal

import json


def read_category_url():
    f = open('category_url.json', 'r')
    f.readline()
    jsonstr = f.readline()
    jsondict = json.loads(jsonstr)
    f.close()
    return jsondict


class DdSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com']
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def parse(self, response):
        category_url = read_category_url()
        books = self.yieldparsebooks(category_url.get('url'))
        return books

    def yieldparsebooks(self, category_url):
        for value in category_url:
            if url_is_legal(value):
                yield scrapy.Request(url=value, callback=self.parsebooks)

    def parsebooks(self, response):
        loader = ItemLoader(item=BookItem(), response=response)
        loader.add_xpath("title", '//ul[@class="bigimg"]/li/a/@title')
        loader.add_xpath("url", '//ul[@class="bigimg"]/li/a/@href')
        items = loader.load_item()
        yield items
        next_page = response.xpath('//li[@class="next"]/a/@href').extract()[0]
        print("====================")
        print(self.start_urls[0] + next_page)
        print("====================")
        if next_page is not None:
            yield scrapy.Request(url=self.start_urls[0] + next_page, callback=self.parsebooks)

    # def yieldmorepages(self, response, category_url):
    #     for value in category_url.values():
    #         if url_is_legal(value):
    #             yield scrapy.Request(url=value, callback=self.parsebooks)
# for index,link in enumerate(path):
#      args = (index, link.xpath('@href').get(), link.xpath('text()').get())
#      print('Link number %d points to url %r and category %r' % args)

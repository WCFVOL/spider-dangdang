import scrapy
from spider.items import CategoryItem
from scrapy.loader import ItemLoader
from spider.util import url_is_legal


def parse_category(response):
    loader = ItemLoader(item=CategoryItem(), response=response)
    loader.add_xpath("category",
                     '//div[@id="floor_1"]/div[@class="classify_kind"]'
                     '/ul[@class="classify_kind_detail"]/li/a/text()')
    loader.add_xpath("url",
                     '//div[@id="floor_1"]/div[@class="classify_kind"]'
                     '/ul[@class="classify_kind_detail"]/li/a/@href')
    items = loader.load_item()
    # {"影视写真": "http://category.dangdang.com/cp01.01.13.00.00.00.html"}
    #result = dict(zip(items.get("category"), items.get("url")))
    return items


class DdSpider(scrapy.Spider):
    name = 'category_url'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com']
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def parse(self, response):
        items = parse_category(response)
        return items
    #     for key in items.keys():
    #         yield scrapy.Request(url=items.get(key),meta={'category':key,'url':items.get(key)}, callback=self.parse_page)
    #
    # def parse_page(self, response):
    #     loader = ItemLoader(item=CategoryItem(), response=response)
    #     loader.add_xpath("category",
    #                      '//div[@id="floor_1"]/div[@class="classify_kind"]'
    #                      '/ul[@class="classify_kind_detail"]/li/a/text()')

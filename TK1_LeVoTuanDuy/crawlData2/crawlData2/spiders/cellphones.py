import scrapy
from crawlData2.items import Crawldata2Item
from w3lib.html import remove_tags
import os, json
import pymongo

class CellphonesSpider(scrapy.Spider):
    name = "cellphones"
    allowed_domains = ["cellphones.com.vn"]
    start_urls = ["https://cellphones.com.vn/mobile/samsung.html"]


    def __init__(self):
        super(CellphonesSpider, self).__init__()
        self.client = pymongo.MongoClient('mongodb+srv://tuanduy:1234@cluster0.sv5osnu.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client["test"]
        self.collection = self.db['cellphones']


    def parse(self, response):
        questionURLs = response.xpath('//div[@class="product-info"]/descendant::a/@href').getall()
        for questionURL in questionURLs:
            item = Crawldata2Item() 
            item['link'] = response.urljoin(questionURL)
            request = scrapy.Request(url = response.urljoin(questionURL), callback=self.parseQA)
            request.meta['item'] = item
            yield request


    def parseQA(self, response):
        item = response.meta['item']
        item['title'] = remove_tags(response.xpath('//div[@class="box-product-name"]/descendant::h1').get()).strip()
        item['price'] = response.xpath('normalize-space(string(//div[@class="box-info__box-price"]/descendant::p[1]))').get()

        yield item
        # Đẩy dữ liệu vào MongoDB
        self.collection.insert_one(dict(item))

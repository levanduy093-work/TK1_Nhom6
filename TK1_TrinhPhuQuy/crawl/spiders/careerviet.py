import scrapy
from crawl.items import CrawlItem
import os,json
import pandas as pd

class CareervietSpider(scrapy.Spider):
    name = "careerviet"
    allowed_domains = ["careerviet.vn"]
    # start_urls = ["https://careerviet.vn"]

    def start_requests(self) :
        for page_number in range(1,2):
            yield scrapy.Request(url='https://careerviet.vn/viec-lam/tat-ca-viec-lam-trang-{page_number}-vi.html'.format(page_number=page_number),callback=self.parse)

    def parse(self, response):
        questionURLs = response.xpath('//div[@class="title "]/descendant::h2/a/@href').getall()
        for questionURLs in questionURLs:
            item = CrawlItem()
            item['Link'] = response.urljoin(questionURLs)
            request = scrapy.Request(url = response.urljoin(questionURLs),callback=self.parseQA)
            request.meta['item'] = item
            yield request

    def parseQA(self,response):
        item = response.meta['item']
        item["Position"] = response.xpath('string(//h1)').get()
        item["Location"] = response.xpath('string(//p/a)').get()
        item["Salary"] = response.xpath('//div[@class="detail-box has-background"]/ul/li/p/text()')[6].get()
        item["DeadlineSummit"] = response.xpath('//div[@class="detail-box has-background"]/ul/li/p/text()')[9].get()
        item["Detail"] = ''.join(response.xpath('//div[@class="detail-row reset-bullet"]/p/text()').getall())
        item["Require"] = ''.join(response.xpath('//div[@class="detail-row"]/p/text()').getall())
        yield item
        # current_dir = os.getcwd()
        # file_path = os.path.join(current_dir,'data1.json')
        # with open(file_path,'a' , encoding='utf-8') as f:
        #     json.dumps({
        #         "Link": item['Link'],
        #          "Position": item['Position'],
        #           "Location": item['Location'],
        #            "Salary": item['Salary'],
        #             "DeadlineSummit": item['DeadlineSummit'],
        #              "Detail": item['Detail'],
        #               "Require": item['Require']
        #     },ensure_ascii=False) +'\n' 
        

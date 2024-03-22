import scrapy
from crawldata.items import CrawldataItem
import os , json
class PhapluatSpider(scrapy.Spider):
    name = "phapluat"
    allowed_domains = ["thuvienphapluat.vn"]
    # start_urls = ["https://thuvienphapluat.vn"]
    def start_requests(self):
        for page_number in range(1,2):
            yield scrapy.Request(url=f'https://thuvienphapluat.vn/phap-luat/so-huu-tri-tue?page={page_number}'.format(page_number),callback=self.parse) 
    
    def parse(self, response):
        questionURLs = response.xpath('//article[contains(@class, "news-card")]/a/@href').getall()
        for questionURL in questionURLs:
            item = CrawldataItem()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url=response.urljoin(questionURL),callback=self.parseQA)
            request.meta['item'] = item
            yield request
#  C1           
    def parseQA(self, response):
        item = response.meta['item']
        item['Lawname'] = "phapluat"
        item['Title'] = response.xpath('normalize-space(string(//h1))').get()
        item['Question'] = response.xpath('normalize-space(string(//section[contains(@class,"news-content")]/strong))').get()
        item['Answer'] = response.xpath('//section[contains(@class,"news-content")]//blockquote//em/text()').getall()
        yield item
#   C2
    # def parseQA(self, response):
    #     item = response.meta['item']
    #     item['Lawname'] = "phapluat"
    #     item['Title'] = response.xpath('normalize-space(string(//h1))').get()
    #     item['Question'] = response.xpath('normalize-space(string(//section[contains(@class,"news-content")]/strong))').get()
    #     # item['Answer'] = response.xpath('normalize-space(string(//section[contains(@class,"news-content")]/blockquote/em))').get()
    #     item['Answer'] = response.xpath('//section[contains(@class,"news-content")]//blockquote//em/text()').getall()
    #     current_dir = os.getcwd()
    #     file_path = os.path.join(current_dir, 'data1.json')
    #     with open(file_path, 'a', encoding='utf-8') as f:
    #         json.dump(dict(item), f, ensure_ascii=False)
    #         f.write('\n')
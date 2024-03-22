import scrapy
from crawldata.items import CrawldataItem
import os, json


class CoursesSpider(scrapy.Spider):
    name = "courses"
    allowed_domains = ["campus.w3schools.com"]
    # start_urls = ["https://campus.w3schools.com"]

    def start_requests(self):
        yield scrapy.Request(url='https://campus.w3schools.com/collections/course-best-sellers', callback=self.parse)

    def parse(self, response):
        questionURLs = response.xpath('//div[@class="productitem"]/descendant::a/@href').getall()
        for questionURL in questionURLs:
            item = CrawldataItem()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url= response.urljoin(questionURL), callback= self.parseQA)
            request.meta['item'] = item
            yield request

    def parseQA(self, response):
        item = response.meta['item']
        item['Name'] = response.xpath('normalize-space(string(//h1[@class="product-title"]))').get()
        item['Pay'] = response.xpath('normalize-space(string(//span[@class="money"]))').get()
        item['Why'] = response.xpath('normalize-space(string(//h2[@class="heading1 image-with-text__heading"]))').get()   
        item['Text_Why'] = response.xpath('normalize-space(string(//div[@class="subheading1 image-with-text__text"]/descendant::p/span))').get()
        item['Learn'] = response.xpath('normalize-space(string(//h2[@class="heading2 image-with-text__heading"]))').get() 
        item['Text_Learn'] = response.xpath('normalize-space(string(//div[@class="subheading2 image-with-text__text"]/descendant::ul))').get()
        yield item

        # current_dir = os.getcwd()
        # file_path = os.path.join(current_dir, 'VuTheKiet.json')
        # with open(file_path , 'a') as f:
        #     line = json.dumps({
        #         'Link' : item['Link'],
        #         'Name': item['Name'],
        #         'Pay': item['Pay'],
        #         'Why': item['Why'],
        #         'Text_Why': item['Text_Why'],
        #         'Learn': item['Learn'],
        #         'Text_Learn': item['Text_Learn']}, ensure_ascii=False) + '\n'
        #     f.write(line)
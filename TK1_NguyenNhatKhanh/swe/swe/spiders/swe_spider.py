import scrapy
from swe.items import SweItem

class SweSpiderSpider(scrapy.Spider):
    name = "swe_spider"
    allowed_domains = ["swe.vn"]
    # start_urls = ["https://swe.vn/"]

    def start_requests(self):
        for page_number in range(1, 4):
            yield scrapy.Request(url = 'https://swe.vn/collections/all?sort_by=new&page={page_number}'.format(page_number = page_number), callback = self.parse)

    def parse(self, response):
        productsURL = response.xpath('//div[@class="row"]/div[@class="col-md-3 col-sm-6 col-xs-6"]/div/div[1]/a/@href').getall()
        for productURL in productsURL:
            item = SweItem()
            item['Link'] = response.urljoin(productURL)
            request = scrapy.Request(url = response.urljoin(productURL), callback = self.parsePrd)
            request.meta['item'] = item
            yield request
    
    def parsePrd(self, response):
        item = response.meta['item']
        item['Name'] = response.xpath('string(//h2)').get()
        item['Price'] = response.xpath('string(//span[@id="pro-price"])').get() 
        item['Size'] = response.xpath('//div[@class="select-swap"]/div/@data-value').getall() 
        item['Image'] = response.xpath('/html/body/main/section/div/div/div[1]/div[2]/div/div//descendant::img/@src').getall()
        item['Detail'] = response.xpath('//div[@class="description clearfix"]/div/div//text()').getall() 

        yield item
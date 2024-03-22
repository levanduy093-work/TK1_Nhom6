# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    Link = scrapy.Field()
    Name = scrapy.Field()
    Pay = scrapy.Field()
    Why = scrapy.Field()
    Text_Why = scrapy.Field()
    Learn = scrapy.Field()
    Text_Learn = scrapy.Field()

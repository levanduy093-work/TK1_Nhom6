# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Link = scrapy.Field()
    Title = scrapy.Field()
    Position = scrapy.Field()
    Location = scrapy.Field()
    Salary = scrapy.Field()
    DeadlineSummit = scrapy.Field()
    Detail = scrapy.Field()
    Require = scrapy.Field()

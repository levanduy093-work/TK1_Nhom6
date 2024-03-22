# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# from pymongo import MongoClient
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobscraperPipeline:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://Khai:1234@ntmkhai.jvblben.mongodb.net/?retryWrites=true&w=majority&appName=NTMKhai')  # Connect to your MongoDB Atlas
        self.db = self.client['data']  
    def process_item(self, item, spider):
        collection = self.db['jobs']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pipeline: {e}")


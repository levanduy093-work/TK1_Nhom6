# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json

class MongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://tuanduy:1234@cluster0.sv5osnu.mongodb.net/?retryWrites=true&w=majority')
        self.db = self.client["test"]

    def process_item(self, item, spider):
        collection = self.db['cellphones']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pipeline: {e}")
class JsonDBPipeline:
    def process_item(self, item, spider):
        self.file = open('test_cellphones.json', 'a', encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii= False) + "\n"
        self.file.write(line)
        self.file.close()
        return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo 
import json
class MonggoDBPipeline:
    def __init__(self):

        self.client = pymongo.MongoClient("mongodb+srv://testadmin:1234@data.teijr6y.mongodb.net/?retryWrites=true&w=majority&appName=Data")
        self.db = self.client["lawnet"]

    def process_item(self, item, spider):
        collection = self.db['phapluat']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pineline:{e}") 

class JsonDBPipeline:
    def process_item(self, item, spider):
        self.file = open('lawnet_phapluat.json','a',encoding='utf-8')
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(line)
        self.file.close()
        return item






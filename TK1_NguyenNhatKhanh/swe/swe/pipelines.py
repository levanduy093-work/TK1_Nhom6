# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json
from scrapy.exceptions import DropItem

# class SwePipeline:
#     def __init__(self):
#         self.client = pymongo.MongoClient('mongodb+srv://sa:sapassword@cluster0.yx3puvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
#         self.db = self.client["swe"]

#     def process_item(self, item, spider):
#         collection = self.db["swe_db"]

#         try:
#             collection.insert_one (dict(item))               
#             return item
#         except Exception as e:
#             raise DropItem(f"Error in pipeline : {e}")
    
# class JsonDBPipeline:
#     def proccess_item(self, item, spider):
#         self.file = open('swe_db.json', 'a', encoding="utf-8")
#         line = json.dumps(dict(item)) + "\n"
#         self.file.write(line)
#         self.file.close()
#         return item
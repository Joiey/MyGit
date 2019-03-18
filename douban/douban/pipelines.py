# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from douban.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME, MONGODB_DOCNAME

class DoubanPipeline(object):
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        sheetname = MONGODB_DOCNAME
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

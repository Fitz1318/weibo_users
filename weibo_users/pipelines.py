# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class MongoPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        #爬虫一旦开启，就会实现这个方法，连接到数据库
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        # 爬虫一旦关闭，就会实现这个方法，关闭数据库连接
        self.client.close()

    def process_item(self, item, spider):
        #每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        # update()起到去重的效果
        self.db['user'].update({'id': item['id']}, {'$set': item}, True)
        return item

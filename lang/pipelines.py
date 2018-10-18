# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re

class LangPipeline(object):
    def open_spider(self,spider):
        self.f=open("news.json","a")
    def close_spider(self,spider):
        self.f.close()
    def process_item(self, item, spider):
        strinfo1=re.compile(' ')
        strinfo2 = re.compile('\n')
        c1=strinfo1.sub('',item['c'][0])
        c2=strinfo2.sub('',c1)
        tp1=item['a'][0]+"   "+item['b'][0]+"   "+c2+"\n"
        self.f.write(tp1)

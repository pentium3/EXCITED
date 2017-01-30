# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import hashlib

class DspPipeline(object):
    def process_item(self, item, spider):
        self.url=item['url']
        self.dictfile=open('site.txt','a')
        self.dictfile.write(self.url)
        self.dictfile.write("\n")
        self.dictfile.close()

        uu =  self.url
        conn = MySQLdb.connect(host='192.168.0.101', user='pdv', passwd='asdfgh', db='url', charset='utf8')
        ss = conn.cursor()
        seq = 'insert into urltable(url,uh) values (%s,%s)'
        para = (uu, hashlib.md5(uu).hexdigest()[8:-8])
        ss.execute(seq, para)
        conn.commit()
        conn.close()

        return item

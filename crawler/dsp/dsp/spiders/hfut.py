# -*- coding: utf-8 -*-
import scrapy
import re
import traceback
import requests
import MySQLdb
import hashlib
from scrapy.selector import HtmlXPathSelector
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.http import Request
from dsp.items import DspItem

from scrapy import optional_features
#optional_features.remove('boto')           #NEEDED BY MACINTOSH

class HfutSpider(RedisSpider):
    name = "dsp"
    allowed_domains = ["hfut.edu.cn"]
    redis_key = 'dsp start_urls'
    start_urls = (
        'http://www.hfut.edu.cn',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
        #RespType=response.headers['Content-Type']
        #if('text/html' in RespType):
            webcontent = DspItem()
            #webcontent['content']=response.body
            webcontent['url']=response.url
            yield webcontent
            lklist=response.xpath('//a/@href').extract()
            lknum=len(lklist)
            purl=response.url

            try:
                conn = MySQLdb.connect(host='192.168.0.101', user='pdv', passwd='asdfgh', db='url', charset='utf8')
                ss = conn.cursor()
                seq = 'insert into graphtable(uh,nout,nin) values (%s,%s,0)'
                para = (hashlib.md5(purl).hexdigest()[8:-8], lknum)
                ss.execute(seq, para)
                conn.commit()
                conn.close()
            except:
                pass

            print("VIEWED::::::",response.url,"        ")
            for lk in lklist:
                lurl=response.urljoin(lk).encode('utf-8')

                try:
                    fu =  response.url
                    su =  lurl
                    fh=hashlib.md5(fu).hexdigest()[8:-8]
                    sh=hashlib.md5(su).hexdigest()[8:-8]
                    conn = MySQLdb.connect(host='192.168.0.101', user='pdv', passwd='asdfgh', db='url', charset='utf8')
                    ss = conn.cursor()
                    seq = "select uid from urltable where uh='%s'" % (fh)
                    ss.execute(seq)
                    ll = ss.fetchall()
                    fid = ll[0][0]
                    seq = "select uid from urltable where uh='%s'" % (sh)
                    ss.execute(seq)
                    ll = ss.fetchall()
                    sid = ll[0][0]
                    seq = 'insert into lnktable(fid,sid) values (%s,%s)'
                    para = (str(fid),str(sid))
                    ss.execute(seq, para)
                    conn.commit()
                    conn.close()
                except:
                    pass

                yield Request(lurl, callback=self.parse)

        except:
            pass


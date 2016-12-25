# -*- coding: utf-8 -*-
import scrapy
import re
import pycurl
import cStringIO
from scrapy.selector import HtmlXPathSelector
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.http import Request
from dsp.items import DspItem

from scrapy import optional_features
optional_features.remove('boto')           #NEEDED BY MACINTOSH

class HfutSpider(RedisSpider):
    name = "dsp"
    allowed_domains = ["sdu.edu.cn"]
    redis_key = 'dsp start_urls'
    start_urls = (
        'http://www.sdu.edu.cn/',
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
            #print("VIEWED::::::",response.url,"-------",response.headers,'--####--',lklist)
            for lk in lklist:
                lurl=response.urljoin(lk).encode('utf-8')
                buf=cStringIO.StringIO()
                c=pycurl.Curl()
                c.setopt(c.URL,lurl)
                c.setopt(c.NOBODY,1)
                c.setopt(c.HEADERFUNCTION,buf.write)
                c.perform()
                RespType=buf.getvalue()
                #print("CRAWL???-----",RespType,"   ",lurl)
                if('text/html' in RespType):
                    yield scrapy.Request(lurl,callback=self.parse)
        except:
            pass


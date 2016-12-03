# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import HtmlXPathSelector
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from scrapy.http import Request
from dsp.items import DspItem

from scrapy import optional_features
optional_features.remove('boto')

class HfutSpider(RedisSpider):
    name = "dsp"
    allowed_domains = ["hfut.edu.cn"]
    redis_key = 'dsp start_urls'
    start_urls = (
        'http://www.hfut.edu.cn/',
    )

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            RespType=response.headers['Content-Type']
            if('text/html' in RespType):
                webcontent = DspItem()
                #webcontent['content']=response.body
                webcontent['url']=response.url
                yield webcontent
                print("VIEWED::::::",response.url,"-------",response.headers)
                for lk in response.xpath('//a/@href').extract():
                    lurl=response.urljoin(lk)
                    #print("CRAWLED::::::", lurl)
                    yield scrapy.Request(lurl,callback=self.parse)
        except:
            pass


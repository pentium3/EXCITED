from scrapy import cmdline
import redis
from dsp.settings import *

dictfile = open('site.txt', 'w')
dictfile.write("\n")
dictfile.close()

print ("SERVER INFO:  ",REDIS_HOST,REDIS_PORT)
rr=redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
rr.flushall()

cmdline.execute("scrapy crawl dsp".split())

# -*- coding: utf-8 -*-

BOT_NAME = 'dsp'

SPIDER_MODULES = ['dsp.spiders']
NEWSPIDER_MODULE = 'dsp.spiders'

DEPTH_LIMIT = 1

DOWNLOAD_DELAY = 2

DOWNLOAD_TIMEOUT=30

DOWNLOAD_MAXSIZE=12582912       #12MB

DEFAULT_REQUEST_HEADERS={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

ITEM_PIPELINES = ['dsp.pipelines.DspPipeline']

SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'
REDIE_URL = None
REDIS_HOST = '172.18.72.5'
REDIS_PORT = 6379
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

DOWNLOADER_HTTPCLIENTFACTORY = 'dsp.downloader.LimitHTTPClientFactory'

#SCHEDULER_IDLE_BEFORE_CLOSE = 10
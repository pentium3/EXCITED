# This snippet was taken from the old wiki.
#
# You can do this by overriding the Scrapy HTTP Client Factory, with the following (undocumented) setting:
#
#     DOWNLOADER_HTTPCLIENTFACTORY = 'myproject.downloader.LimitHTTPClientFactory'
#

MAX_RESPONSE_SIZE = 1048576  # 1Mb

from scrapy.core.downloader.webclient import ScrapyHTTPClientFactory, ScrapyHTTPPageGetter


class LimitPageGetter(ScrapyHTTPPageGetter):
    def handleHeader(self, key, value):
        ScrapyHTTPPageGetter.handleHeader(self, key, value)
        # if key.lower() == 'content-length' and int(value) > MAX_RESPONSE_SIZE:
        #     self.connectionLost('oversized')
        #     print("XXXXXXXXXXXXXX")
        if key.lower() == 'content-type' and value.lower() != 'text/html':
            self.connectionLost('unqualified_type')
            print("TTTTTTTTTTTTTT")


class LimitHTTPClientFactory(ScrapyHTTPClientFactory):
    protocol = LimitPageGetter

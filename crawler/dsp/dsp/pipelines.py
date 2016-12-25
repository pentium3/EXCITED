# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DspPipeline(object):
    def process_item(self, item, spider):
        self.url=item['url']
        self.dictfile=open('site.txt','a')
        self.dictfile.write(self.url)
        self.dictfile.write("\n")
        self.dictfile.close()

        #self.eurl=item['url'].replace('/','_').replace(":","")
        #self.filename=self.eurl+''
        #self.file=open(self.filename,'wb')
        #print("WRITEFILE::::::",self.filename)
        #self.file.write(item['content'])
        #self.file.close()
        return item

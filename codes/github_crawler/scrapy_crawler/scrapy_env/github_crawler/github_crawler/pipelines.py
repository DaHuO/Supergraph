# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GithubCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
    	start_urls = ['https://github.com/search?l=Python&q=sorting&type=Repositories']
    	spider.init_start_urls(start_urls)

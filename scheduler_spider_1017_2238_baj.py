# 代码生成时间: 2025-10-17 22:38:33
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from twisted.internet.error import ReactorNotRunning
from apscheduler.schedulers.background import BackgroundScheduler
import logging

# 设置日志记录
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def parse(self, response):
        # 解析响应并提取数据
        logging.info('Parsing %s', response.url)
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, self.parse)

    def closed(self, reason):
        # 关闭时执行的任务
        logging.info('Spider closed: %s', reason)

class SchedulerSpider(scrapy.Spider):
    name = 'scheduler_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def __init__(self, *args, **kwargs):
        super(SchedulerSpider, self).__init__(*args, **kwargs)
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.run_spider, 'interval', hours=1)
        self.scheduler.start()

    def run_spider(self):
        try:
            # 运行Scrapy爬虫
            process = CrawlerProcess()
            process.crawl(MySpider)
            process.start()
        except Exception as e:
            logging.error('Error running spider: %s', str(e))

    def closed(self, reason):
        # 关闭时执行的任务
        logging.info('Scheduler spider closed: %s', reason)
        try:
            self.scheduler.shutdown()
        except ReactorNotRunning:
            logging.error('Reactor not running during shutdown')

if __name__ == '__main__':
    # 创建Scrapy爬虫
    spider = SchedulerSpider()
    spider.start_requests()

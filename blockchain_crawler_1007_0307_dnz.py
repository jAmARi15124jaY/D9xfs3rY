# 代码生成时间: 2025-10-07 03:07:21
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.utils.project import get_project_settings
from twisted.internet.error import DNSLookupError, TimeoutError, TCP4ConnectionError


# Define a custom Spider for Blockchain Crawler
class BlockchainSpider(scrapy.Spider):
    name = 'blockchain_crawler'
    allowed_domains = []  # Define the domains you want to crawl
    start_urls = []  # Define the starting URLs for the spider

    # Custom initialization method
    def __init__(self, *args, **kwargs):
        super(BlockchainSpider, self).__init__(*args, **kwargs)
        self.settings = get_project_settings()
        self.domains = self.settings.get('DOMAINS')
        self.start_urls = self.settings.get('START_URLS')

    # Method to handle the response from the start URLs
    def parse(self, response):
        try:
            # Extract data and yield or process it
            # For example, extract transactions or blocks
            for transaction in response.xpath('//transaction'):
                yield {
                    'blockchain': response.meta['blockchain'],
                    'txid': transaction.xpath('./@txid').get(),
                    'amount': transaction.xpath('./@amount').get(),
                }
            # Follow links to next pages or related pages
            next_page = response.css('a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)
        except Exception as e:
            self.logger.error(f'Error parsing {response.url}: {e}')
            raise CloseSpider('Parse error')

    # Handle DNS Lookup errors
    def handle_dns_error(self, failure):
        if failure.check(DNSLookupError):
            self.logger.error('DNSLookupError on %s', self.name)
            raise CloseSpider('DNSLookupError')

    # Handle Timeout errors
    def handle_timeout_error(self, failure):
        if failure.check(TimeoutError):
            self.logger.error('TimeoutError on %s', self.name)
            raise CloseSpider('TimeoutError')

    # Handle TCP4Connection errors
    def handle_connection_error(self, failure):
        if failure.check(TCP4ConnectionError):
            self.logger.error('TCP4ConnectionError on %s', self.name)
            raise CloseSpider('TCP4ConnectionError')


# Define a method to run the spider
def run_crawler():
    process = CrawlerProcess()
    process.crawl(BlockchainSpider)
    process.start()  # the script will block here until all crawling jobs are finished


# If the script is executed directly, run the crawler
if __name__ == '__main__':
    run_crawler()
# 代码生成时间: 2025-09-23 21:13:01
import scrapy
import random
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

"""
Test Data Generator

This script uses Scrapy framework to generate test data.
It is designed to be easily understandable, maintainable, and extensible.

Usage:
    python test_data_generator.py
"""

# Define a Spider class to generate test data
class TestDataSpider(scrapy.Spider):
    name = 'test_data'
    start_urls = ['http://example.com/']  # Example URL, replace with your target website

    def parse(self, response):
        # Generate test data
        test_data = {
            'id': random.randint(1, 100),
            'name': f'Name{random.randint(1, 100)}',
            'age': random.randint(18, 99),
            'city': random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']),
            'gender': random.choice(['Male', 'Female']),
        }

        # Print the generated test data
        self.log(f'Generated Test Data: {test_data}')
        yield test_data

    def closed(self, reason):
        # Handle any cleanup or finalization after the spider is closed
        self.log(f'Spider closed: {reason}')

# Main function to run the Scrapy spider
def main():
    try:
        # Create a Scrapy CrawlerProcess with default settings
        process = CrawlerProcess(get_project_settings())

        # Add the TestDataSpider to the process
        process.crawl(TestDataSpider)

        # Start the crawling process
        process.start()
    except Exception as e:
        # Handle any errors that occur during the crawling process
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
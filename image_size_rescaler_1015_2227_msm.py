# 代码生成时间: 2025-10-15 22:27:39
import os
from PIL import Image
from scrapy import Spider, Request
from scrapy.crawler import CrawlerProcess

"""
Image Size Rescaler Spider:
This spider is designed to crawl a website, download images,
and resize them to a specified dimension.
"""

class ImageSizeRescaler(Spider):
    name = 'image_size_rescaler'
    start_urls = ['http://example.com/']  # Replace with the actual URL

    def __init__(self, target_size=(100, 100), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_size = target_size

    def parse(self, response):
        # Find all images in the response
        images = response.css('img::attr(src)::text').getall()
        for image_url in images:
            yield Request(url=image_url, callback=self.download_and_resize)

    def download_and_resize(self, response):
        try:
            # Open and resize the image
            with Image.open(response.body) as img:
                resized_image = img.resize(self.target_size)
                # Save the resized image
                filename = os.path.basename(response.url)
                resize_path = f'resized/{filename}'
                resized_image.save(resize_path)
                self.log(f'Image saved to {resize_path}')
        except IOError as e:
            self.log(f'Error resizing image: {e}')

# Set up the CrawlerProcess
process = CrawlerProcess()
process.crawl(ImageSizeRescaler)
process.start()

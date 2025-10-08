# 代码生成时间: 2025-10-08 17:33:45
import psutil
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.exceptions import NotConfigured

"""
Process Manager
A Scrapy extension that manages processes for a Scrapy spider.
"""

class ProcessManager:
    def __init__(self, process_count=1):
        # Initialize the process manager with the desired number of processes
        self.process_count = process_count
        self.processes = []

    def start_processes(self):
        """
        Start the specified number of processes and run the spider in each.
        """
        settings = get_project_settings()
        if not settings.get('BOT_NAME'):
            raise NotConfigured("BOT_NAME setting is required")
        for _ in range(self.process_count):
            # Create a new process for running the spider
            process = CrawlerProcess(settings)
            # Add a signal handler to catch the spider closed signal
            process.signals.connect(self.spider_closed, signal=signals.spider_closed)
            # Start the spider in the process
            process.crawl(MySpider)  # Replace MySpider with your spider class
            process.start()  # Start the process
            self.processes.append(process)

    def spider_closed(self, spider):
        """
        Signal handler for spider closed signal.
        """
        # Remove the process from the list of processes
        for process in self.processes:
            if process.spider is spider:
                self.processes.remove(process)
                break

    def stop_processes(self):
        """
        Stop all running processes.
        """
        for process in self.processes:
            process.stop()

    def get_processes(self):
        """
        Get a list of running processes.
        """
        return self.processes

    def is_process_running(self, process):
        """
        Check if a process is running.
        """
        return process.is_running()

    def get_process_count(self):
        """
        Get the number of processes.
        """
        return len(self.processes)

# Example usage
if __name__ == '__main__':
    process_manager = ProcessManager(process_count=4)
    try:
        process_manager.start_processes()
        # Your code here
    except NotConfigured as e:
        print(f"Error: {e}")
    finally:
        process_manager.stop_processes()

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from cars_scraper.spiders.car_spider import AutoRiaSpider


def run_scraper():
    print("Running scraper...")
    process = CrawlerProcess(get_project_settings())
    process.crawl(AutoRiaSpider)
    process.start()
    print("Scraper finished.")

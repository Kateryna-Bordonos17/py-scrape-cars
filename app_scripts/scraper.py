from scrapy.crawler import CrawlerProcess
from cars_scraper.spiders.car_spider import AutoRiaSpider


def run_scraper():
    process = CrawlerProcess(settings={
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36",
    })

    process.crawl(AutoRiaSpider)
    process.start()

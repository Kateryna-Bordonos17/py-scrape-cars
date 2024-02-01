import re
from datetime import datetime
from scrapy.http import Response

import scrapy

from cars_scraper.items import CarsScraperItem


class AutoRiaSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com/uk/car/used/"]

    # Uncomment this if you want to scrape a few pages
    # max_pages = 5
    # pages_parsed = 0

    def parse(self, response: Response, **kwargs):
        # Uncomment this if you want to scrape a few pages
        # if self.pages_parsed >= self.max_pages:
        #     self.log("Reached the maximum number of pages to parse. Stopping.")
        #     return

        for car in response.css(".ticket-item"):
            cars_page = car.css(".head-ticket a::attr(href)").get()
            yield response.follow(url=cars_page,
                                  callback=self.parse_cars)

        # Uncomment this if you want to scrape a few pages
        # self.pages_parsed += 1

        next_page = response.css(".pager > span")[-1].css("a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def parse_cars(response: Response):
        item = CarsScraperItem()

        item["url"] = response.url
        item["title"] = response.css("h1::text").get()
        price_usd = response.css("strong::text").get()
        item["price_usd"] = int(re.sub(r'\D', '', price_usd))
        item["odometer"] = response.css("dd.mhide span:nth-child(2)::text").get().replace(" тис. км", "000")
        item["username"] = response.css(".seller_info_name::text").get()
        item["image_url"] = response.css(".photo-620x465:first-child img::attr(src)").get()
        item["images_count"] = len(response.css(".photo-620x465"))
        item["car_number"] = response.css(".state-num::text").get()
        item["car_vin"] = response.css(".label-vin::text").get() or response.css(".vin-code::text").get()
        item["datetime_found"] = datetime.now()

        yield item

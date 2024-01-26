from datetime import datetime
from scrapy.http import Response

import scrapy


class AutoRiaSpider(scrapy.Spider):
    name = "cars"
    allowed_domains = ["auto.ria.com"]
    start_urls = ["https://auto.ria.com/uk/car/used/"]

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.driver = webdriver.Chrome()
    #
    # def close(self, reason):
    #     self.driver.close()

    def parse(self, response: Response, **kwargs):
        for car in response.css(".ticket-item"):
            cars_page = car.css(".head-ticket a::attr(href)").get()
            yield response.follow(url=cars_page,
                                  callback=self.parse_cars)

        next_page = response.css(".pager > span")[-1].css("a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    @staticmethod
    def parse_cars(response: Response):
        yield {
            "url":
                response.url,
            "title":
                response.css("h1::text").get(),
            "price_usd":
                int(response.css("strong::text").get().replace(" ", "").replace("$", "")),
            "odometer":
                response.css("dd.mhide span:nth-child(2)::text").get().replace(" тис. км", "000"),
            "username":
                response.css(".seller_info_name::text").get(),
            # "phone_number":
            #     response.css(".phone::text").get(),
            "image_url":
                response.css(".photo-620x465:first-child img::attr(src)").get(),
            "images_count":
                len(response.css(".photo-620x465")),
            "car_number":
                response.css(".state-num::text").get(),
            "car_vin":
                response.css(".label-vin::text").get() or response.css(".vin-code::text").get(),
            "datetime_found":
                datetime.now()
        }

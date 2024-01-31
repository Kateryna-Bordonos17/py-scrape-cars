# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarsScraperItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price_usd = scrapy.Field()
    odometer = scrapy.Field()
    username = scrapy.Field()
    image_url = scrapy.Field()
    images_count = scrapy.Field()
    car_number = scrapy.Field()
    car_vin = scrapy.Field()
    datetime_found = scrapy.Field()

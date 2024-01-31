# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# car_scraper/pipelines.py

import psycopg2
from scrapy.exceptions import DropItem
from cars_scraper import settings
from cars_scraper.items import CarsScraperItem


class CarsScraperPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.DATABASES["default"]["HOST"],
            port=settings.DATABASES["default"]["PORT"],
            user=settings.DATABASES["default"]["USER"],
            password=settings.DATABASES["default"]["PASSWORD"],
            database=settings.DATABASES["default"]["NAME"]
        )
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS cars (
                    id SERIAL PRIMARY KEY,
                    url VARCHAR(255),
                    title VARCHAR(255),
                    price_usd INTEGER,
                    odometer INTEGER,
                    username VARCHAR(255),
                    image_url VARCHAR(255),
                    images_count INTEGER,
                    car_number VARCHAR(20),
                    car_vin VARCHAR(50),
                    datetime_found TIMESTAMP,
                    datetime_saved TIMESTAMP
                )
                """
            )
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise DropItem(f"Failed to create table in the database: {e}")

    def process_item(self, item: CarsScraperItem, spider):
        try:
            self.cursor.execute("SELECT id FROM cars WHERE car_vin = %s LIMIT 1", (item["car_vin"],))
            existing_record = self.cursor.fetchone()

            if existing_record:
                # If a record with the same car_vin exists, skip insertion
                spider.logger.info(f"Duplicate record found for car_vin: {item['car_vin']}")
                return item

            current_datetime = datetime.now()

            self.cursor.execute(
                """
                INSERT INTO cars (url, 
                                  title, 
                                  price_usd, 
                                  odometer, 
                                  username,
                                  image_url, 
                                  images_count, 
                                  car_number, 
                                  car_vin, 
                                  datetime_found, 
                                  datetime_saved)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    item["url"],
                    item["title"],
                    item["price_usd"],
                    item["odometer"],
                    item["username"],
                    item["image_url"],
                    item["images_count"],
                    item["car_number"],
                    item["car_vin"],
                    item["datetime_found"],
                    current_datetime
                )
            )
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise DropItem(f"Failed to insert item into the database: {e}")

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

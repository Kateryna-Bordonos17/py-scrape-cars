import psycopg2
from scrapy.exceptions import DropItem

from cars_scraper import settings


connection = psycopg2.connect(
    host=settings.DATABASES["default"]["HOST"],
    port=settings.DATABASES["default"]["PORT"],
    user=settings.DATABASES["default"]["USER"],
    password=settings.DATABASES["default"]["PASSWORD"],
    database=settings.DATABASES["default"]["NAME"]
)
cursor = connection.cursor()


def create_table():
    try:
        cursor.execute(
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
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise DropItem(f"Failed to create table in the database: {e}")

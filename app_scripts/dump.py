import os
from datetime import datetime
import psycopg2

from cars_scraper import settings


def create_dump():
    connection = psycopg2.connect(
        host=settings.DATABASES["default"]["HOST"],
        port=settings.DATABASES["default"]["PORT"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        database=settings.DATABASES["default"]["NAME"]
    )
    cursor = connection.cursor()

    dumps_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dumps")
    os.makedirs(dumps_directory, exist_ok=True)
    dump_filename = os.path.join(dumps_directory,
                                 f"db_dump_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql")

    cursor.execute("SELECT * FROM cars")
    data = cursor.fetchall()

    with open(dump_filename, "w") as dump_file:
        for row in data:
            dump_file.write(str(row) + "\n")

    print(f"Database dump created: {dump_filename}")

    cursor.close()
    connection.close()

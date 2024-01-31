import schedule

from cars_scraper.settings import SCRAPER_SCHEDULE_TIME, DUMP_SCHEDULE_TIME
from app_scripts.scraper import run_scraper
from app_scripts.dump import create_dump


def main():
    schedule.every().day.at(SCRAPER_SCHEDULE_TIME).do(run_scraper)
    schedule.every().day.at(DUMP_SCHEDULE_TIME).do(create_dump)
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()

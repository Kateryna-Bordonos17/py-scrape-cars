# Car Scraper

## About

The application is designed for periodic scraping of the [AutoRia](https://auto.ria.com/car/used/) platform, specifically for used cars. The application is scheduled to run every day at a specified time and iterates through all pages starting from the initial page to the end. For each car listing, it enters the individual car details page and collects the necessary data.

## Features
- Automated scraping on a scheduled basis
- Regularly scheduled database backups
- Application containerized using Docker


## Technologies
- Python
- PostgreSQL
- Scrapy
- Docker

## Requirements
- Clone the repository:
```angular2html
git clone git@github.com:Katherine-Greg/py-scrape-cars.git
```

- If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```angular2html
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

- Run app:
```angular2html
python main.py
```

- or Run it with Docker
```angular2html
docker-compose up
```

- If you want to check spider`s work, run
```angular2html
scrapy crawl cars
```

# How to Contribute
- Create a branch for the solution and switch on it:
```angular2html
git checkout -b develop
```

Feel free to add more data, and implement new methods and features!

- Save the solution:
```angular2html
git commit -am 'Solution'
```

- Push the solution to the repo:
```angular2html
git push origin develop
```

If you created another branch (not develop) use its name instead

Create `New Pull Request`:
- Go to the original repository on GitHub and click on the New Pull Request.

- Provide details about your changes and submit the pull request for review.


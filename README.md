# Botnoi Final Project
This project is the final project for Botnoi Python Classroom Module 2: Web Scraping. The goal is to use web scraper to obtain data from [Thairath website](www.thairath.co.th), the biggest newspaper in Thailand, in any of the following categories: 

   - [royal](https://www.thairath.co.th/news/royal)
   - [local](https://www.thairath.co.th/news/local)
   - [business](https://www.thairath.co.th/news/royal) <- This repository selects this category
   - [foreign](https://www.thairath.co.th/news/royal)
   - [society](https://www.thairath.co.th/news/royal)
   - [crime](https://www.thairath.co.th/news/royal)

The target scraped data should contains the following entities: *title*, *published_date*, *content*, *tags*, *cover_img*, *news_url*, *category*. These data is stored in MongoDB. The script is run on Heroku and scheduled to scrape every 1 hour.

Another Flask WebAPI is deployed in Heroku to allow users to request data from the database with filters as follows:

- date - show only news in a specific date
- tag - show only news with given tags
- limit - limit number of news to be shown
- date and tag simultaneously

# Working Process
This project started by quick prototyping of the scraper in Jupyter Notebook. This allows us to find target elements in the webpage, test scraping commands, and create a step-by-step documentation.

All tested commands are assembled and refactored in the final script before deploying with a scheduler in Heroku. This repo requires *Heroku Scheduler* and *mLab MongoDB* add-ons. The first one allows us to schedule the scraper to run every given amount of time. Another one creates a simple noSQL database and stores the scraped data there.

Please create a database in mLab and make sure that the database's URI is stored in your environment variable. Then simply use command `python scraper_app.py` in the scheduler and that's it.

The data in the database can be access by another [project](https://github.com/peeraponw/Thairathnews_flask) which is running [here](https://thairath-news-api.herokuapp.com/api?date=2020-07-17&limit=2&tag=%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99) 

# Relavant Technologies
- Heroku
- Flask
- WebAPI
- MongoDB
- BeautifulSoup
- Selenium

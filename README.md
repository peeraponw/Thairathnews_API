# Botnoi Final Project
This project is the final project for Botnoi Python Classroom Module 2: Web Scraping. The goal is to use web scraper to obtain data from [Thairath website](www.thairath.co.th), the biggest newspaper in Thailand, in any of the following categories: 

   - [royal](https://www.thairath.co.th/news/royal)
   - [local](https://www.thairath.co.th/news/local)
   - [business](https://www.thairath.co.th/news/royal) <- This repository select this category
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
This project started by quick prototyping in Jupyter Notebook. This allows us to find target elements in the webpage, test scraping commands, and create a step-by-step documentation.

A Flask local app was then 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0MjE1OTU0NV19
-->
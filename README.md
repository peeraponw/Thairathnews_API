# Botnoi Final Project
This project is the final project for Botnoi Python Classroom Module 2: Web Scraping. The goal is to use web scraper to obtain data from [Thairath website](www.thairath.co.th), the biggest newspaper in Thailand, in any of the following categories: 

   - [royal](https://www.thairath.co.th/news/royal)
 
   - [local](https://www.thairath.co.th/news/local)

   - [business](https://www.thairath.co.th/news/royal)

   - [foreign](https://www.thairath.co.th/news/royal)

   - [society](https://www.thairath.co.th/news/royal)

   - [crime](https://www.thairath.co.th/news/royal)

The target scraped data should contains the following entities: *title*, *published_date*, *content*, *tags*, *cover_img*, *news_url*, *category*. These data is stored in MongoDB. The script is run on Heroku and scheduled to scrape every 1 hour.

A Flask WebAPI is developed to allow users to request data from the database with the following fil



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NDI5NDI5MTNdfQ==
-->
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
from flask import Flask, jsonify, request
from datetime import datetime
import json

# def connect_db():

def scrape_data(url):
    driver = webdriver.Chrome('C:\Program Files\Google\chromedriver.exe')
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.close()
    sel = soup.find('h3', text='ข่าวอื่นๆ').find_next('div').find_all('a')


    # collect news links and images. Prepare to navigate through these links.

    news = {'title': [], 'pub_date': [], 'content': [], 'tags': [], 'cover_img': [], 'url': [], 'cat': []}
    for i, s in enumerate(sel):
        if i%2 == 1:
            continue
        # get url
        news['url'].append('https://www.thairath.co.th'+s['href']) 
        # get cover_img url
        news['cover_img'].append(s.find('img')['src'])
        # get title
        news['title'].append(s.find('img')['alt'])
        # get category
        news['cat'].append(news['url'][-1].split('/')[4])

    for news_url in news['url']:
        driver = webdriver.Chrome('C:\Program Files\Google\chromedriver.exe')
        driver.get(news_url)
        
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # get time
        t = datetime.strptime(soup.find('meta', property='article:published_time')['content'][:-6], '%Y-%m-%dT%H:%M:%S')
        news['pub_date'].append(t.strftime('%Y-%m-%d'))
        # get tags
        tags = soup.find('h2', text='แท็กที่เกี่ยวข้อง').find_next('div').find_all('span')
        tag_l = []
        for tag in tags:
            tag_l.append(tag.text)
        news['tags'].append(tag_l)
        # get content
        contents = soup.find('article', id='article-content').find_all('p')
        news['content'].append(''.join([c.text for c in contents]))
        driver.close()
        
    return news
    


# def insert_to_db():

def main():
    news = scrape_data('https://www.thairath.co.th/news/business')
    print(news)
if __name__=="__main__":
    main()
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
from flask import Flask, jsonify, request
from datetime import datetime
import json
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


def connect_db():
    db_uri = os.environ.get('MONGODB_URI')
    client = MongoClient(db_uri, retryWrites=False)
    db = client['heroku_95w86hmz']
    collection_name = 'thairath'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    collection = db[collection_name]
    return collection

def scrape_data(url):
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), 
                                chrome_options=chrome_options)
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
    print(news['url'])
    for news_url in news['url'][0:5]:
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
        
    # reformulate the news
    docs = []
    for i in range(0, len(news['content'])):
        docs.append({
            'title': news['title'][i],
            'pub_date': news['pub_date'][i],
            'content': news['content'][i],
            'tags': news['tags'][i],
            'cover_img': news['cover_img'][i],
            'url': news['url'][i],
            'cat': news['cat'][i]
        })
    return docs
    


def insert_to_db(collection, docs):
    for document in docs:
        
        if not collection.find_one(document):
            collection.insert_one(document)
    
        

def main():
    docs = scrape_data('https://www.thairath.co.th/news/business')
    collection = connect_db()    
    insert_to_db(collection, docs)


if __name__=="__main__":
    main()
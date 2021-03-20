from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

mars = {}


#Mars News - collect the title and paragraph text

news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

slid = news_soup.select_one('ul.item_list li.slide')

news_title = slid.find('div', class_='content_title').get_text()
news_article = slid.find('div', class_='article_teaser_body').get_text()
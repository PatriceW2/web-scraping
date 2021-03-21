from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)



#Mars News - collect the title and paragraph text

news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

slid = news_soup.select_one('ul.item_list li.slide')

news_title = slid.find('div', class_='content_title').get_text()
news_article = slid.find('div', class_='article_teaser_body').get_text()


print(news_title)
print(news_article)

browser.quit()

#JPL Mars Space Image - Featured Image 



image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(image_url)
html = browser.html
image_soup = soup(html, 'html.parser')

print(image_soup)


image = image_soup.find('div', class_='header')
image = image.find('img', class_='headerimage fade-in')


image_source = image.get('src')
image_source = (image_url+image_source).replace('index.html', '')

print(image_source)


#Hemispheres 

hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemi_url)
html = browser.html
hemi_soup = soup(html, 'html.parser')

hemi_items = soup.find_all('div', class_='item')

hemi_img_url = []

for item in hemi_items:
    title = item.find('h3').text
    browser.click_link_by_partial_text(title)   
    
    html = browser.html
    hemi_img_soup = soup(html, 'html.parser')
    
    find_img = hemi_img_soup.find('a', text="Sample")
    img_url = find_img['href']
    
    hemi_img_url.apppend({'title': title, 'img_url': img_url})
    
    browser.back()
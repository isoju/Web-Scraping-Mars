#listing dependencies
from bs4 import BeautifulSoup as bs
import pymongo
import requests
from flask import Flask, render_template
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


def test_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless = False)

def scrape():
    
    browser = test_browser()
    

    ##NASA Mars News
    nasa_mars_news_url = 'https://redplanetscience.com/'
    browser.visit(nasa_mars_news_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    #putting date, title, and p into variables
    latest_date = soup.find_all('div', class_ = 'list_date')[0].text
    news_title = soup.find_all('div', class_ = 'content_title')[0].text
    news_p = soup.find_all('div', class_ = 'article_teaser_body')[0].text


    ##JPL Mars Space Images - Featured Image
    jpl_url = 'https://spaceimages-mars.com/'
    browser.visit(jpl_url)

    html = browser.html
    soup = bs(html, 'html.parser')
    feature_image = soup.find_all('img', class_ = 'headerimage')[0]['src']

    featured_image_url = jpl_url + feature_image


    ##Mars Facts
    facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)

    mars_table = tables[1]
    mars_table  =mars_table.rename(columns = {0:"Label", 1:"Value"})
    mars_table = mars_table.set_index("Label")

    mars_table_html = mars_table.to_html()

    ##Mars Hemispheres
    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)
    html  = browser.html
    soup = bs(html, 'html.parser')

    #trying to get links to each hemi
    div_item = soup.find_all('a', class_ = 'itemLink')
    # div_item
    hemi_list = []
    for x in div_item:
        hemi_html = x['href']
        hemi_list.append(hemi_html)

    #cleaning list of hemi htmls
    hemi_list = list(set(hemi_list))
    hemi_list = [y for y in hemi_list if ".html" in y]

    hemisphere_image_urls = []
    for hemi in hemi_list:
        browser.visit(hemi_url + hemi)
        html = browser.html
        soup = bs(html, 'html.parser')
        title = soup.find('h2', class_ = 'title').text
        hemi_img_li = soup.find_all('li')[0]
        hemi_img = hemi_img_li.find('a')['href']
        img_url = hemi_url + hemi_img
        hemi_dict = {
            "title": title,
            "img_url": img_url
        }
        hemisphere_image_urls.append(hemi_dict)


    #return dict with all scraped data
    ultimate_dict = {}
    ultimate_dict = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "Mars_table": mars_table_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()
    return ultimate_dict

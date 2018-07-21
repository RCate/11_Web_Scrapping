
# Scraping


# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time



# Retrieve page with the requests module
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# NASA Mars News

def scrape_News():

    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html
    Mars_soup = BeautifulSoup(html, 'html.parser')

# Extract title text
    News_title = Mars_soup.find('div',class_="content_title").a.text
# Extract the Paragraph info under the Title. 
    # News_paragraphs = Mars_soup.find('div',class_="article_teaser_body").text
    News_paragraphs = Mars_soup.find('div',class_="image_and_description_container").text
    news = {
        "News_title": News_title,
        "News_paragraphs": News_paragraphs
    }
    return news

# Featured Image works in Jupiter Notebook - but not in this app because of Javascript changing the path... 
#I completed the web-scrap, but just didn't get it to load into this file - nor into the HTLM portion

# def scrape_image():
#     image_browser = init_browser()

#     image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     image_browser.visit(image_url)
#     time.sleep(5)

#     img = image_browser.find_by_id('full_image')
#     img.click()

#     html_2 = image_browser.html

#     image_soup_2 = BeautifulSoup(html_2, 'html.parser')
#     with open("image_soup_2.html", "w") as fwrite:
#         fwrite.write(html_2)
#     featured_image_url = image_soup_2.select(".fancybox-image") #[0]['src']
#     with open("featured_image_url.html", "w") as fwrite:
#         fwrite.write(featured_image_url)
#     image = {
#         "featured_image_url": featured_image_url
#     }
#     return image

# # Mars Weather

def scrape_weather():
    Mars_Weather_URL = 'https://twitter.com/MarsWxReport/status/1017925917065302016'
    Weather_response = requests.get(Mars_Weather_URL)
# Create BeautifulSoup object; parse with 'html.parser'
    Weather_soup = BeautifulSoup(Weather_response.text, 'html.parser')

    mars_weather = Weather_soup.find('p',class_="TweetTextSize").text
    weather = {
        "mars_weather": mars_weather
    }
    return weather


#  Mars Facts

import pandas as pd
def scrape_table_info():
    Mars_Facts_URL = 'https://space-facts.com/mars/'
    Mars_tables = pd.read_html(Mars_Facts_URL)
    Mars_tables[0]

    Mars_df = Mars_tables[0]
    Mars_df.columns = ['0', '1']
    Mars_df.rename(columns = {'0':'Mars Information', '1': 'Facts'}, inplace = True)
    Mars_df

    Mars_HTML = Mars_df.to_html(classes = "table table-striped")
    mars_tables = {
        "Table": Mars_HTML
    }
    return mars_tables



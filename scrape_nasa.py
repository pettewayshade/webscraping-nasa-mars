from splinter import Browser
from bs4 import BeautifulSoup ad bs
import urllib2
import pandas as pd
import time

def init_browser():
	executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Broweser("chrome", **executable_path, headless=True)

def scrape_info():

    #read in  urls of websites from file
    list_open = open("sites.txt")
    read_list = list_open.read()
    line_in_list = read_list.split("\n")

    browser = init_browser()

    counter = 0
    for url in line_in_list:
            counter +=1
            browser.visit(url)

            time.sleep(1)

            soup = bs(urllib2.urlopen(url).read(), 'html.parser')
            
            #get data we are looking for
            if counter == 1:
                #get data from first site
                news_title = ""
                news_p = ""

            if counter == 2:
                #get data from second site
                featured_image_url = ""

            if counter == 3:
                #get data from third site
                url = 'https://space-facts.com/mars/'
                ldf = pd.read_html(url)
                mars_facts = ldf[0]

            if counter == 4:
                #get data from 4th site:
                text = []

            if counter == 5:
                images = []
            #close brower session
            browser.quit()

    #dict to store data
    mars_data = {
            "news_title": news_title,
            "news_p": news_p,
            "mars_facts": mars_facts,
            "mars_weather": mars_weather,
            "featured_image_url": featured_image_url,
            "images": images
    }

    #return the results
    return mars_data

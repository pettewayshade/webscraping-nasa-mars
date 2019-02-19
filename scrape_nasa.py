from splinter import Browser
from bs4 import BeautifulSoup ad bs
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
    
    for url in line_in_list:
            browser.visit(url)

            time.sleep(1)

            soup = bs(urllib2.urlopen(url).read(), 'html.parser')
            



            #get data we are looking for
            news_title = ""

            news_p = ""


            #dict to store data
            mars_data = {
                    "news_title": news_tile,
                    "news_p": news_p
            }

            #close browser session after scraping
            browser.quit()

    #return the results
    return mars_data

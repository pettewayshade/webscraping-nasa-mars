from splinter import Browser
from bs4 import BeautifulSoup ad bs
import time

def init_browser():
	executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Broweser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    url = ("https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+" +
            "desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest")
    browser.visit(url)

    time.sleep(1)


    #scrape page
    html = browser.html
    soup = bs(html, "html.parser")

    #get data we are looking for


    #close browser session after scraping
    browser.quit()

    #return the results
    return mars_data

from splinter import Browser
from bs4 import BeautifulSoup as bs
import urllib
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scrape_info():

    #read in  urls of websites from file
    list_open = open("sites.txt")
    read_list = list_open.read()
    line_in_list = read_list.split("\n")

    browser = init_browser()

    counter = 0
    for url in line_in_list:
        try:
            counter +=1
            browser.visit(url)

            time.sleep(1)

            html = browser.html
            soup = bs(html, 'html.parser')
            
            #get data we are looking for
            if counter == 1:
                #get data from first site, NASA Mars News Site:
                news_title = soup.find('div', class_='content_title').get_text()
                news_p = soup.find('div', class_='article_teaser_body').get_text()

            if counter == 2:
                #get data from second site, JPL Featured Space Image:
                url ='https://www.jpl.nasa.gov'
                li_element = soup.find('li', class_='slide')
                featured_image_url = li_element.a['data-fancybox-href']
                featured_image_url = url + featured_image_url
            
            if counter == 3:
                #get data from third site
                url = 'https://space-facts.com/mars/'
                ldf = pd.read_html(url)
                ldf =ldf[0]
                ldf.columns = ["Description", "Values"]
                ldf.set_index(["Description"])
                ldf = ldf.to_html()
                mars_facts = ldf

            if counter == 4:
                #get data from 4th site, Twitter:
                mars_weather = soup.find_all('p', 
                        class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].get_text()

            if counter == 5:
                imgs = soup.find_all('div', class_="item")
                imgDict = {}
                hemisphere_image_urls = list(imgDict)        
        except:
            continue

            
    #dict to store data
    mars_data = {
            "news_title": news_title,
            "news_p": news_p,
            "mars_facts": mars_facts,
            "mars_weather": mars_weather,
            "featured_image_url": featured_image_url,
            "images": hemisphere_image_urls
    }

    browser.quit()

    #return the results
    return mars_data

if __name__ == '__main__':
    data = scrape_info()
    print (data)

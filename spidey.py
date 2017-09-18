import requests
from bs4 import BeautifulSoup
import random
import urllib

#function to download pictures from the links of image sources
def download_web(url):
    name=random.randrange(1,2000)
    full=str(name)
    urllib.urlretrieve(url,full)

#function to crawl the website and send the links of all the images to the download_web()
def spidy():

    url=raw_input("Enter the url    ")
    src=requests.get(url)
    text=src.text
    soup=BeautifulSoup(text,"html.parser")
    for img in soup.findAll('img'):
             image=img.get('src')
             #Sometimes the links of images are incomplete.
             #Like they dont have https:// which makes the link invalid
             #Here we are checking if the crawled link is complete or not.
             #if it is complete,then its cool
             #otherwise we just add https:// to the incomplete link
             if image[0]=='h':
                 complete = image

             else:
                 complete = "https:" + image

             print(complete)
             download_web(complete)

spidy()








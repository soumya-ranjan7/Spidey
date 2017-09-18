import requests
from bs4 import BeautifulSoup
import random
import urllib

def download_web(url):
    name=random.randrange(1,2000)
    full=str(name)
    urllib.urlretrieve(url,full)


def spidy():

    url=raw_input("Enter the url    ")
    src=requests.get(url)
    text=src.text
    soup=BeautifulSoup(text,"html.parser")
    for img in soup.findAll('img'):
             image=img.get('src')

             if image[0]=='h':
                 complete = image

             else:
                 complete = "https:" + image

             print(complete)
             download_web(image)

spidy()








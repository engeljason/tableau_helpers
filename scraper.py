import requests, zipfile, io
from bs4 import BeautifulSoup
from splinter import Browser
import time

def get_page(url):
    executable_path = {"executable_path": "C:/Users/Jason/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    browser.quit()
    return html

def get_soup(url):
    html = get_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def downloadZip(url):
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("./resources/data")

index_url = "https://s3.amazonaws.com/tripdata/index.html"
r = get_soup(index_url)
allA = r.find_all('a')

for a in allA:
    if a.endswith('.zip'):
        downloadZip(a['href'])

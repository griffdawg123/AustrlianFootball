import os
import hashlib
import requests
from bs4 import BeautifulSoup

if not os.path.exists('.cache'):
    os.makedirs('.cache')

ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'
session = requests.Session()

def get(url):
    '''Return cached lxml tree for url'''
    path = os.path.join('.cache', hashlib.md5(url.encode('utf-8')).hexdigest() + '.html')
    if not os.path.exists(path):
        print(url)
        response = session.get(url, headers={'User-Agent': ua})
        with open(path, 'w', encoding='utf-8') as fd:
            fd.write(response.text)
    return BeautifulSoup(open(path, encoding='utf-8'), 'html.parser')
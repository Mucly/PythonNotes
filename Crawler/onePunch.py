import re
from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen

ENTRANCE_URL = "http://yqcr.17dm.com/manhua/"
url = requests.get(ENTRANCE_URL).content.decode('gbk', 'ignore')
soup = BeautifulSoup(url, features='lxml')
chapter_urls = soup.find_all('a', {'href': re.compile(f'{ENTRANCE_URL}\d+\.html')})
chapter_urls = [a['href'] for a in chapter_urls]

for chapter in chapter_urls:
    url = requests.get(chapter).content.decode('gbk', 'ignore')
    soup = BeautifulSoup(url)
    page_cnt = soup.find('select', {'name': 'listNarImg'})
    page_cnt = len(page_cnt.find_all('option', {'value': re.compile(r'\d' +)}))

    for cnt in range(page_cnt):
        url = requests.get(f'{ENTRANCE_URL}')

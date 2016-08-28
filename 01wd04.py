from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import time
import random

originURL = 'http://weheartit.com/inspirations/taylorswift'
dirPath = './pic-01wd04/'  # need to complete some judgement

webDataRaw = requests.get(originURL)
webData = webDataRaw.text
soup = BeautifulSoup(webData, 'lxml')

picBag = soup.select('#main-container > div:nth-of-type(2) > div > div > div > div > a > img')

for ipic in picBag:

    picURL = ipic.get('src')
    extensionName = picURL[-4:]
    fileName = picURL[len('http://data.whicdn.com/images/'):][:(-len('/superthumb.jpg'))] + extensionName
    fullName = dirPath + fileName

    urlretrieve(picURL, fullName)
    print('Done')
    time.sleep(random.randrange(random.randrange(5,10), random.randrange(10, 15))) # random in random to achieve anti-anti-crawling
    #time.sleep(random.randint(random.randint(5)))


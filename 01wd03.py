#coding: utf-8
from bs4 import BeautifulSoup as bs
import requests

# CONSTANTS
FEMALE_TIP = '\xe5\xa5\xb9'
GENDER_TIP = u'\u6027\u522b\uff1a'
FEMALE = '\xe5\xa5\xb3'
MALE = '\xe7\x94\xb7'

# Source
urlFather = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
webDataFather = requests.get(urlFather)
soupFather = bs(webDataFather.text, 'lxml')
url = (soupFather.select('#page_list > ul > li > a'))[0].get('href')
webData = requests.get(url)
soup = bs(webData.text, 'lxml')

# Raw data
title = [i.get_text() for i in soup.select('div.pho_info > h4 > em')][0]
address = [i.get_text() for i in soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')][0]
feed_pd = [i.get_text() for i in soup.select('#pricePart > div.day_l > span')][0]
imgHouse001 = [i.get('src') for i in soup.select('#curBigImage')][0]

nameLandlord = [i.get('title') for i in soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')][0]
imgLandlord = [i.get('src') for i in soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')][0]
profileURL = [i.get('href') for i in soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')][0]
profileGet = requests.get(profileURL)
profileSoup = bs(profileGet.text, 'lxml')

if 0 == len(profileSoup.find_all("ul", class_="fd_person")):
    genderStatement = [i.get_text() for i in profileSoup.select('body > div.contentFD.clearfix > div.fd_con > \
div.fd_infor > dl > dt')][0]
    if FEMALE_TIP == genderStatement[0].encode('utf-8'):
        gender = FEMALE
    else:
        gender = MALE
else:
    gender = [i.get_text() for i in profileSoup.select('ul.fd_person > li:nth-of-type(1)')][0].strip(GENDER_TIP).encode('utf-8')

print('[Title] {}\n[Address] {}\n[Price] {}\n[Image URL(download it and open in Chrome)] {}'.format(title.encode('utf-8'), address.encode('utf-8'),
                                                                                                    feed_pd, imgHouse001))
print('[Information about the landlord]')
print('    [Name  ] {}'.format(nameLandlord.encode('utf-8')))
print('    [Gender] {}'.format(gender))
print('    [Image ] {}'.format(imgLandlord))


'''
# The following code is part of a trial(unfinished, but n),
# try to crawl information from http://bj.xiaozhu.com/search-duanzufang-p1-0/

# Preparation for the whole website

urlFather = 'http://bj.xiaozhu.com/search-duanzufang-p1-0/'
webDataFather = requests.get(urlFather)
soupFather = bs(webDataFather.text, 'lxml')
linkList = soupFather.select('#page_list > ul > li > a')


title = []

for iLink in linkList:
    # Preparation for each
    urlEach = iLink.get('href')
    webDataEach = requests.get(urlEach)
    soupEach = bs(webDataEach.text, 'lxml')

    # Get the data
    tempTitleList = soupEach.select('div.pho_info > h4 > em')
    title.extend(tempTitleList)


for i in title:
    print(i.get_text())

'''
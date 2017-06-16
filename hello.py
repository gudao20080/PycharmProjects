#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
from http import cookiejar
from urllib import request

if __name__ == '__main__':
    webUrl = 'http://wise.xmu.edu.cn/people/faculty'
    # resp = request.urlopen(webUrl)
    # html = resp.read().decode('utf-8')
    # print(html)
    # resp = requests.get(webUrl)
    #
    #
    # soup = BeautifulSoup(resp.content, 'html.parser')
    # # print('header', header)
    #
    # peopleList = soup.find('div', attrs={'class': 'people_list'})
    # a_s = peopleList.find_all('a', attrs={'target': '_blank'})
    #
    # for a in a_s:
    #     url = a['href']
    #     name = a.get_text()
    #     print(name, url)

    # cookie = cookiejar.CookieJar()
    # handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(handler)
    # response = opener.open(webUrl)
    # for item in cookie:
    #     print('name = %s ' % item.name)
    #     print('value = %s ' % item.value)


    fileName = 'D:\cookie.txt'
    cookie = cookiejar.MozillaCookieJar(fileName)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(webUrl)
    cookie.save(ignore_discard=True, ignore_expires=True)

    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    for item in cookie:
        print('name = %s ' % item.name)
        print('value = %s ' % item.value)


#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    webUrl = 'http://wise.xmu.edu.cn/people/faculty'
    # resp = request.urlopen(webUrl)
    # html = resp.read().decode('utf-8')
    # print(html)
    resp = requests.get(webUrl)


    soup = BeautifulSoup(resp.content, 'html.parser')
    # print('header', header)

    peopleList = soup.find('div', attrs={'class': 'people_list'})
    a_s = peopleList.find_all('a', attrs={'target': '_blank'})

    for a in a_s:
        url = a['href']
        name = a.get_text()
        print(name, url)



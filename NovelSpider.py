import requests
from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    novelUrl = 'http://www.biqukan.com/1_1094/'
    # novelUrl = 'http://www.baidu.com/'
    headers = {}

    headers['User-Agent'] = ' Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 58.0; .3029; .81; Safari / 537.36'

    req = request.Request(novelUrl, headers=headers)
    response = request.urlopen(novelUrl)
    data = response.read()
    soup = BeautifulSoup(data, 'lxml')

    list_main = soup.find('div', attrs={'class': 'listmain'})
    dl_soup = list_main.find('dl')
    # print(list_main)
    print(dl_soup)
    flag = False
    for item in dl_soup:
        print(item.contents)


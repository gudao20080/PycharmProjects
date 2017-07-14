from collections import OrderedDict

import requests
from urllib import request

import time

from bs4 import BeautifulSoup
import chardet


def gain_novel_segments(html_doc: str):

    soup = BeautifulSoup(html_doc, 'lxml')

    soup_dl = soup.dl
    # print(soup_dl)

    novel_map = OrderedDict()
    dl_count = 0
    for item in soup_dl.children:
        # print(item)

        if item and item.name:
            if item.name == 'dt':
                dl_count += 1

            if dl_count > 1 and item.name == 'dd':
                a_tag = item.a
                href = a_tag['href']
                segment_title = a_tag.text
                segment_url = "http://www.biqukan.com" + href
                novel_map[segment_title] = segment_url
                # print('{href:100} {title}'.format(href=segment_url, title=segment_title))

    return novel_map


def gain_html_doc(url: str):
    '''
    获取html页面

    :param url: 网页url
    :return: 获取到的html页面内容
    '''

    if url and type(url) == str:
        headers = {}
        headers['User-Agent'] = ' Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 58.0; .3029; .81; Safari / 537.36'
        req = request.Request(url, headers=headers)
        response = request.urlopen(req)
        data_bytes = response.read()
        char_set = chardet.detect(data_bytes)['encoding']

        html_doc = data_bytes.decode(char_set, 'ignore')
        return html_doc


    else:
        raise TypeError('url 错误')


def parseNovelHtml(html_doc: str, file_path: str):

    soup = BeautifulSoup(html_doc, 'lxml')
    content_tag = soup.find('div', attrs={'class': "showtxt", 'id': "content"})

    tile_tag = soup.find('meta', attrs={'name': 'keywords'})
    title = tile_tag['content']
    f = open(file_path, 'a')
    f.write(title)
    f.write('\n' * 3)

    for item in content_tag.children:
        # f.write(item.te)
        if item.name == 'br':
            f.write('\n\n')
        else:
            f.write(item.replace('\xa0', ' '))

        print(item, type(item))

    f.write('\n' * 3)
    f.close()
    # return content_tag.text

if __name__ == '__main__':
    # novelUrl = 'http://www.biqukan.com/1_1094/'
    novelUrl = 'http://www.biqukan.com/11_11025/4088520.html'

    chapter_list_doc = gain_html_doc(novelUrl)
    f = open("D:/cc.txt", 'w', encoding='utf-8')
    f.write(chapter_list_doc)
    print(chapter_list_doc)
    # segments = gain_novel_segments(chapter_list_doc)


    print(len(segments))
    # print(segments)
    i = 0

    for k, v in segments.items():
        print(k, v)
        segment_content = gain_html_doc(v)
        parseNovelHtml(segment_content, "D:/一念永恒.txt")
        time.sleep(3)

        # if i == 0:
        # with open("D:/一念永恒.txt", 'a') as f:
        #     if segment_content:
        #         f.write(k)
        #         f.write('\n\n\n')
        #         f.write(segment_content.replace(u'\xa0', u''))
        #         break
        # i += 1

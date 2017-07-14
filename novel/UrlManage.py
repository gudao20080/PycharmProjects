from collections import OrderedDict
from bs4 import BeautifulSoup, NavigableString
from urllib import request, response


# http://www.biqukan.com
class UrlManager(object):
    def __init__(self, novel_url: str) -> None:
        self.novel_url = novel_url

    def crawlWeb(self) -> BeautifulSoup:
        headers = {}
        headers[
            'User-Agent'] = ' Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like; Gecko) Chrome / 58.0; .3029; .81; Safari / 537.36'
        req = request.Request(self.novel_url, headers=headers)
        response = request.urlopen(req)
        data_bytes = response.read()
        # print(data_bytes.decode('gbk'))
        soup = BeautifulSoup(data_bytes, 'lxml')
        return soup

    def parseSectionsBs4(self, soup: BeautifulSoup) -> OrderedDict:
        list_soup = soup.find("div", attrs={"class": "listmain"})
        # print(list_soup)
        filter_list_soup = list_soup.find_all('a')
        # print(filter_list_soup)
        ordered_dict = OrderedDict()
        for item in filter_list_soup:
            # print(item)
            # print(item['href'], item.get_text(strip=True))
            section_title = item.get_text(strip=True)
            section_url = "http://www.biqukan.com" + item['href']
            ordered_dict[section_title] = section_url

        return ordered_dict

    s = ""
    def parseSection(self, soup: BeautifulSoup) -> tuple:
        content_soup = soup.find('div', attrs={"class": "content"})
        title = content_soup.h1.get_text()
        # print(type(title))
        # print(soup)
        global s

        content_tag = content_soup.find('div', attrs={"id": "content", 'class': 'showtxt'})
        for child in content_tag.children:
            if type(child) is NavigableString:
                # print(child)
                s.join(child)

        print("ss: ", s)
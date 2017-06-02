import requests
from bs4 import BeautifulSoup


class Url_manager(object):
    def __init__(self) -> None:
        self.new_urls = set()
        self.old_urls = set()

    def add_url(self, url: str):
        if url is None:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        else:
            self.new_urls.add(url)

    def get_new_urls(self):
        return self.new_urls

class ParserContent(object):
    def __init__(self) -> None:
        self.title = None
        self.desc = None
        self.urls = set()

class Download_manager(object):
    def __init__(self) -> None:
        pass

    def download(self, url: str):
        response = requests.get(url)
        return response.content

    def save(self, content: ParserContent):

        with open(r'D:\baike.html', 'a') as f:
            f.write('<html>')
            f.write('<body>')
            f.write('<table border="3">')
            f.write('<tr>')
            f.write('<td>')
            f.write(content.title)
            f.write('</td>')
            # f.write('<td>')
            # f.write(content.desc)
            # f.write('</td>')


            f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')




class Parser_manager(object):

    def parser(self, html: str):
        if html is None:
            return

        content = ParserContent()
        soup = BeautifulSoup(html, 'html.parser')
        dd_node = soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'})
        title = dd_node.find('h1').get_text()
        content.title = title

        desc_node = soup.find('div', attrs={'class': 'lemma-summary'})
        desc_list = desc_node.find_all('a')
        # desc = ' ,'.join([x.get_text() for x in desc_list])
        content.desc = desc_list[0].get_text() + desc_list[1].get_text()
        # content.desc = desc_node.get_text()
        return content





class Spider_manager(object):
    def __init__(self) -> None:
        self.url_manager = Url_manager()
        self.download_manager = Download_manager()
        self.parser_manager = Parser_manager()

    def start(self, url: str):
        self.url_manager.add_url(url)
        new_urls = self.url_manager.new_urls
        # while len(new_urls) > 0:

        for download_url in new_urls:
            htmlData = self.download_manager.download(download_url)
            content = self.parser_manager.parser(htmlData)
            self.download_manager.save(content)

        self.url_manager.new_urls.remove(download_url)
        self.url_manager.old_urls.add(download_url)


if __name__ == '__main__':
    baike_url = 'http://baike.baidu.com/link?url=DuUl3rSfIUZjQA_WXlYxL4xbCDdJ_2gJXYkkDZQMal9Cv3N5978RSx8rMtW2ADsmoxCAiEiTzyXFTVizub5VdK'

    spider = Spider_manager()
    spider.start(baike_url)

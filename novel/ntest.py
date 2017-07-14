from novel.UrlManage import UrlManager
import re
from collections import OrderedDict

url = "http://www.biqukan.com/11_11025/"

# manager = UrlManager(url)
# sections_soup = manager.crawlWeb()
# sections_dict = manager.parseSectionsBs4(sections_soup)
#
#
# def fund(key: tuple):
#     # print(key)
#     re_match = re.search(r'\d+', key[0])
#     if re_match and re_match.group(0):
#         return int(re_match.group(0))
#     else:
#         print('no match: ', key)
#         return 10000
#
#
# l = list(sections_dict.items())
#
# ordered_list = sorted(l, key=fund)
# for item in ordered_list:
#     print(item)

# for key in sections_dict.keys():
#     print(key)
#     print(fund(key))

section_url = "http://www.biqukan.com/11_11025/4088520.html"

manager = UrlManager(section_url)
section_soup = manager.crawlWeb()
# print(section_soup)
manager.parseSection(section_soup)
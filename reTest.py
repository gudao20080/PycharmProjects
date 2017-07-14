import re
from urllib import request, response
import chardet
import time

# url = " http://www.qiushibaike.com/hot/page/1"
#
# heads = {
#     "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
# }
#
#
# req = request.Request(url, headers=heads)
# resp = request.urlopen(req)
# data_bir = resp.read()
# encoding = chardet.detect(data_bir)['encoding']
# print(encoding)
# data = data_bir.decode(encoding)
#
# print(data)
#
# re.compile(r'<div ')
import calendar


# ticks = time.time()
# print(ticks)
#
# localtime = time.localtime(ticks)
# print("localtime: ", localtime)
#
# asctime = time.asctime(localtime)
# print(asctime)
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
# print(time.strftime("%Y %m %d %H %M %S %z %a %A %b %B %c %I %p", localtime))
#
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
#
#
# print('================')
# month = calendar.month(2017, 7, w=10, l=1)
# print(month)
#
# print(time.clock())
import os
import socket

# gethostname = socket.gethostname()
# print(gethostname)
#
# host = socket.gethostbyname(gethostname)
# print(host)
#
# ex = socket.gethostbyname_ex(gethostname)
# print(ex)
#
# # for item in ex:
# #     if isinstance(item, list):
# #         pass
# # print(os.system('ls'))
#
# import subprocess
# f = open("D:/a.txt", "w")
# p = subprocess.Popen('ipconfig', shell=True, stdout=f, stderr=f)
# f.close()
#
# print(p)

import requests

s = "dafd462.第461章 一路风景"
# re_match = re.match(r'.*(\D\d+.*)', s)
# print(re_match.group(1))

# re_search = re.search(r'\d+', s)

# print(re_search.group(0))
# print(re_search.groups())
# print(re_match.group(1))
# print(re_search.group(0))
# print(re_search.group(1))
# re_findall = re.findall(r'\d+', s)
# print(re_findall)


s = ''

def ad():
    global s
    for i in range(1, 100):
        s = s + str(i)
    print(s)

ad()
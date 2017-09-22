from http.cookiejar import CookieJar, FileCookieJar

import requests
import re
import scrapy
from urllib import request
import urllib
import chardet
from http.cookiejar import FileCookieJar, MozillaCookieJar, CookieJar


if __name__ == "__main__":
    url = "http://cuiqingcai.com/954.html"
    url = "https://www.baidu.com/"
    # url = "http://www.whatismyip.com.tw/"

    # req = request.Request(url)
    # req.set_proxy("")
    # req.headers = {}
    # req.method

    # cookie_jar = CookieJar()
    file_name = 'D:/cookie.txt'
    cookie_jar = MozillaCookieJar(file_name)

    #创建cookieJar处理器
    cookiejar_processor = request.HTTPCookieProcessor(cookie_jar)
    # #通过cookieJar处理器来创建opener
    # opener = request.build_opener(proxy_handler)
    # opener.open(url)

    proxy_handler = request.ProxyHandler(proxies={"http":"61.163.39.70:9999"})
    build_opener = request.build_opener(proxy_handler, cookiejar_processor)
    build_opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]

    # opener_open = build_opener.open(url)
    request.install_opener(build_opener)

    urlopen = request.urlopen(url, timeout=10)
    open_read = urlopen.read()
    encoding_ = chardet.detect(open_read)['encoding']

    if not encoding_:
        encoding_ = 'utf-8'
    data = open_read.decode(encoding_)
    # print(data)
    # for item in cookie_jar:
    #     print(item.name, "---------------", item.value)

    cookie_jar.save()
    mozilla_cookie_jar = MozillaCookieJar(file_name)
    mozilla_cookie_jar.load()
    print(mozilla_cookie_jar)
    for item in mozilla_cookie_jar:
        print(item.name, item.value)


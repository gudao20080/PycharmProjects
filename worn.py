import http.cookiejar
import re
import gzip
import json
import os
import re
import threading
import urllib.request

import _thread

import time
from urllib import parse, request
from urllib import error

import chardet

class MyThread(threading.Thread):
    def __init__(self, link: str, filePath: str):
        threading.Thread.__init__(self)
        self.link = link
        self.filePath = filePath

    def run(self):
        print(self.link)
        urllib.request.urlretrieve(self.link, self.filePath)


targetDir = r'F:\pythonDown'


def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos + 1:])
    return t


def downLoadInNewThread(link: str, filePath: str):
    print(filePath)
    urllib.request.urlretrieve(link, filePath)


def savaFile(data):
    savePath = r'D:\temp.txt'
    f = open(savePath, 'wb')
    f.write(data)
    f.close()


def createFormDict(i: str):
    formDict = {}
    formDict['i'] = 'name'
    formDict['from'] = 'UTO'
    formDict['to'] = 'AUTO'
    formDict['smartresult'] = 'dict'
    formDict['client'] = 'fanyideskweb'
    formDict['salt'] = '1495857046111'
    formDict['sign'] = '4a8f3538338c3c1dd5f37b50d2de91ef'
    formDict['doctype'] = 'json'
    formDict['version'] = '2.1'
    formDict['keyfrom'] = 'fanyi.web'
    formDict['action'] = 'FY_BY_CLICKBUTTON'
    formDict['typoResult'] = 'true'
    return formDict


def getOpenner(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    build_opener = urllib.request.build_opener(pro)
    headers = []
    for key, value in head.items():
        elem = (key, value)
        headers.append(elem)

    build_opener.addheaders = headers
    return build_opener

def unGzig(data):
    try:
        print('正在解压')
        data = gzip.decompress(data)
        print('解压完成')
    except:
        print('未经压缩，无需解压')

    return data

def getSource(data):
    re_compile = re.compile(r'name="source" value="(.*)"', 0)

    strList = re_compile.findall(data)
    return strList


if __name__ == '__main__':
    # webUrl = 'http://www.douban.com/'
    webHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    #
    #
    # req = urllib.request.Request(webUrl, headers=webHeader)
    # response = urllib.request.urlopen(req)
    #
    # responseUrl = response.geturl()
    # response_info = response.info()
    # response_getcode = response.getcode()
    # print(" =========", responseUrl)
    # print(" =========", response_info)
    # print(" =========", response_getcode)
    #
    # contentBytes = response.read()
    # detect = chardet.detect(contentBytes)
    # data = contentBytes.decode(detect['encoding'])
    # print(detect)
    # savaFile(contentBytes)
    # for link, t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(contentBytes))):
    #     print(link)
    #     try:
    #         filePath = destFile(link)
    #         # urllib.request.urlretrieve(link, filePath)
    #
    #         # down = downLoadInNewThread(link, filePath)
    #         # _thread.start_new_thread(downLoadInNewThread, (link, filePath,))
    #         thread = MyThread(link, filePath)
    #         thread.start()
    #         # _thread.start_new_thread(print_time, ("Thread-2", 4,))
    #
    #     except:
    #         print("失败")
    #
    # while 1:
    #     pass

    # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
    # req = urllib.request.Request(url)
    # form_dict = createFormDict('name')
    # form_dict__encode = parse.urlencode(form_dict).encode('utf-8')
    # try:
    #     resp = urllib.request.urlopen(url, form_dict__encode)
    #     bData = resp.read()
    #     charSetStr = chardet.detect(bData)
    #     htmlStr = bData.decode()
    #
    #     jsonObj = json.loads(htmlStr)
    #     print('翻译的结果是: {}'.format(jsonObj['translateResult'][0][0]['tgt']))
    #
    #     print(htmlStr)
    # except error.URLError as e:
    #     if hasattr(e, 'code'):
    #         print(e.code)
    #     else:
    #         print(e.reason)

    # url = 'http://www.whatismyip.com.tw/'
    # proxy = {'http': '139.224.237.33:8888'}
    # proxyHandler = request.ProxyHandler(proxy)
    # opener = request.build_opener(proxyHandler)
    # opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # install_opener = request.install_opener(opener)
    # resp = request.urlopen(url)
    # data = resp.read()
    # print(data.decode('utf-8'))



    url = 'https://www.douban.com/accounts/login'
    opener = getOpenner(webHeader)
    op = opener.open(url)
    data = op.read()
    data = unGzig(data)
    decodeData = data.decode()
    print(decodeData)

    source = getSource(decodeData)
    postDict = {
        'source': 'index_nav',
        'form_email': '13323103080',
        'form_password': 'a275892441',
        'remember': 'on'
    }

    postData = urllib.parse.urlencode(postDict).encode()
    opener_open = opener.open(url, postData)
    data = opener_open.read()
    data = unGzig(data)
    print('===================================')
    print(data.decode())




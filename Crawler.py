import urllib.request, urllib.response

com = "http://www.baidu.com"
urlResponse = urllib.request.urlopen(com)
response = urlResponse.read()
print(type(urlResponse))
data = response.decode('utf-8')
print(data)

from abc import ABCMeta, abstractclassmethod


class IStream(metaclass=ABCMeta):
    @abstractclassmethod
    def read(self, maxbytes=-1):
        pass

    @abstractclassmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    pass


import time
from functools import wraps


def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n: int):
    while n > 0:
        n -= 1



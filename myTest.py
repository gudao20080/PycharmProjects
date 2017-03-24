#
# # 创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接
# s.connect(("www.sina.com.cn", 80))
# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
# print(data)
# s.close()

# def user_logging(func):
#     def wrapper():
#         print("%s is running" % func.__name__)
#         return func()
#
#     return wrapper
#
#
# @user_logging
# def foo():
#     print('I am foo')
#
#
# # foo = user_logging(foo)
# foo()

# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warn("%s is running" % func.__name__)
#             elif level == "info":
#                 logging.info("%s is running" % func.__name__)
#             return func(*args)
#
#         return wrapper
#
#     return decorator
#
#
# @use_logging(level="warn")
# def foo(name='foo'):
#     print("i am %s" % name)
#
#
# foo()


# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self):
#
#         print('class decorator runing')
#         self._func()
#         print('class decorator ending')
#
#
# @Foo
# def bar():
#     print('bar')
#
# bar()

# a = "aaaaaaaaaaaaaaa"
# b = "bb"
# c = a + \
#     b
# a = b = c = 1
# print(a)
# print(b)
# print(c)
#
# a, b, c = 1, 2, "name"
# print(a)
# print(b)
# print(c)
# a = 1
# b = 4 + 3j
# print(type(a))
# print(type(b))

#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#
#     while True:
#
#         yield n
#         n += 1
#         if n >= 30:
#             return
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# print('dddddddd', type(f))
# while True:
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()

# sum = lambda x, y: x + y
# print(sum(10, 30))
#
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i, v in enumerate(basket):
#     print(i, v)
#
#
# import sys
#
# for i in sys.argv:
#     print(i)
#
#
# print(sys.path)
#
# import Application
# print(dir(Application))

# import sound.effects.echo
# from sound.effects import echo
#
# echo.convert()
# echo.convert()

# import sound.effects.echo
#
#
# sound.effects.echo.convert()

#
# from sound.effects.echo import convert
#
# convert()
#
# f = open('fool.txt', 'wb')
# f.write(bytes("heool", 'utf8'))
# f.close()
#
# f = open('fool.txt', 'r')
# s = f.read()
# f.close()
# print(s)
#
# f = open('fool.txt', 'a')
# print(f.tell())
# f.write("world")
# f.close()
#
# f = open('fool.txt', 'r')
# print(f.tell())
# s = f.read()
# f.close()
# print(s)
#
# # pickle模块实现序列化和反序列化
# import pickle
#
# data1 = {'a': [1, 2.0, 3, 4 + 6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# out = open('data.pkl', 'wb')
# pickle._dump(data1, out)
#
# pickle._dump(selfref_list, out, -1)
#
# out.close()
#
# import pprint
#
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# print(data2)
#
# pkl_file.close()
#
# import os, sys
#
#
# ret = os.access('data.pkl', os.F_OK)
# print(ret)
#
# try:
#     print(os.getcwd())
#     raise NameError('hehehehheheheheheeheh')
# except (RuntimeError, ValueError, NameError) as err:
#     print('err is {0}'.format(err))
#
#     raise
#
# from timeit import Timer

import time
import threading

# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         # print('{} : % {}'.format(threadName, time.ctime(time.time())))
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         print(threading.current_thread().getName())
#
#
# # 创建两个线程
#
# try:
#     threading._start_new_thread(print_time, ('Thread_1', 2,))
#     threading._start_new_thread(print_time, ('Thread_2', 3,))
#
#     thread = threading.current_thread()
# except:
#     print('Error: 无法启动线程')
#
#
# while 1:
#     pass

# lock = threading.Lock()
#
# class MyThread(threading.Thread):
#     def __init__(self, threadId, name, counter):
#         threading.Thread.__init__(self)
#         self.threadId = threadId
#         self.name = name
#         self.counter = counter
#
#
#     def run(self):
#         print('开户线程：' + self.name)
#         # 获取锁，用于线程同步
#         lock.acquire()
#         print_time(self.name, self.counter, 3)
#         lock.release()
#
#
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1



import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == 'movie':
            print('**********moive**************')
            title = attrs['title']

    # 元素调用结束

    def endElement(self, name):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


# if __name__ == '__main__':
#     # 创建一个XMLReader
#     parser = xml.sax.make_parser()
#
#     # 打开命名空间
#     parser.setFeature(xml.sax.handler.feature_namespaces, 0)
#
#     # 重写ContentHandler
#     handler = MovieHandler()
#     parser.setContentHandler(handler)
#
#     parser.parse('movies.xml')

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 xml 文档
domTree = xml.dom.minidom.parse('movies.xml')
collection = domTree.documentElement
if collection.hasAttribute('shelf'):
    print('Root element : %s ' % collection.getAttribute('shelf'))

# 在集合中获取所有电影
movies = collection.getElementsByTagName('movie')
for movie in movies:
    print('************movie******************')
    if movie.hasAttribute('title'):
        print('Title: %s ' % movie.getAttribute('title'))

import json


import time

ticks = time.time()
print('当前时间： ' , ticks)

localTime = time.localtime(time.time())
print('本地时间： ', localTime)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar

cal = calendar.month(2016, 8)
print('2016 1的日历')
print(cal)

time_clock = time.clock()
print('time_clock: ', time_clock)
time_clock = time.clock()
print('time_clock: ', time_clock)

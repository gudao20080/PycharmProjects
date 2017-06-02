from urllib.request import urlopen


# items = [1, 2, 3]
# it = iter(items)
#
#
# class Node:
#     def __init__(self, value):
#         self._value = value
#         self._children = []
#
#     def __repr__(self):
#         return 'Node({!r})'.format(self._value)
#
#     def add_child(self, node):
#         self._children.append(node)
#
#     def __iter__(self):
#         return iter(self._children)
#
#     def depth_first(self):
#         yield self
#         for c in self:
#             yield from c.depth_first()
#
#
# class Countdown:
#     def __init__(self, start):
#
#         self.start = start
#
#     # Forward iterator
#     def __iter__(self):
#
#         n = self.start
#
#         while n > 0:
#             yield n
#             n -= 1
#
#     # Reverse iterator
#     def __reversed__(self):
#
#         n = 1
#         while n <= self.start:
#             yield n
#             n += 1
#
#
# # for r in iter(Countdown(30)):
# #     print(r)
#
#
#
# def count(n):
#     while True:
#         yield n
#         n += 1
#
#
# # 迭代器和生成器不能使用标准的切片操作， 因为它们的长度事先我们并不知道(并且也没有实现索引)，函数islice()返回一个可以生成指定元素的迭代器，
# # 它通过遍历并丢弃直到切片开始索引位置的所有元素
#
# c = count(0)
# import itertools
#
# for x in itertools.islice(c, 10, 20):
#     print(x)
#
# items = ['a', 'b', 'c']
# from itertools import permutations
#
# for p in permutations(items, 3):
#     print(p)
#
# print("======================")
#
# from itertools import combinations
#
# for c in combinations(items, 3):
#     print(c)
#
# print("======================")
# from itertools import combinations_with_replacement
#
# for c in combinations_with_replacement(items, 3):
#     print(c)
#
# import sys
#
# f = open("fool.txt")
# for chunk in iter(lambda: f.read(10), ''):
#     n = sys.stdout.write(chunk)
#     print(n)
#
# f = open("fool.txt", 'r')
# f.read()
# print()
#
# import csv
#
# # with open("stocks.csv") as f:
# #     f_csv = csv.reader(f)
# #     headers = next(f_csv)
# #     print(headers)
# #     for row in f_csv:
# #         print(row)
#
# headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
# rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
#          'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
#         {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
#          'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
#         {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
#          'Time': '9:36am', 'Change': -0.46, 'Volume': 935000}]
#
# # with open("stocks.csv", 'w') as f:
# #     f_csv = csv.DictWriter(f, headers)
# #     f_csv.writeheader()
# #     f_csv.writerows(rows)
#
# data = {
#     'name': 'ACME',
#     'shares': 100,
#     'price': 542.23
# }
#
# import json
#
# json_str = json.dumps(data)
# print(json_str)
# print(json.loads(json_str))
#
# from xml.etree.ElementTree import parse
#
# u = urlopen('http://planet.python.org/rss20.xml')
# doc = parse(u)
#
# print(doc)


# class LazyConnection(object):
#     __slots__ = ['year', 'month', 'day']
#
#     def __init__(self, address):
#
#
#     def __enter__(self):
#         pass
#
#     def __exit__(self, exc_type, exc_val, exc_tb):


# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('A.__init__')
#
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('B.__init__')
#
#
# class C(A, B):
#     def __init__(self):
#         super().__init__()  # Only one call to super() here
#         print('C.__init__')
#
#
# c = C()


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')

        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


# s = SubPerson("Guido")
# print(s.name)

class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
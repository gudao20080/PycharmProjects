import heapq

import sys

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)

for tag, *x in records:
    print(tag, x)

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=5)  # 使用deque(maxlen=N)会新建一个固定大小的队列
    for line in lines:
        if pattern in line:
            yield line, previous_lines

        print('...')
        previous_lines.append(line)


# if __name__ == '__main__':
#     with open(r'fool.txt') as f:
#         for line, prevLines in search(f, "python", 5):
#             for pline in prevLines:
#                 print("pline: ", pline, end='')
#             print("line: ", line, end='')
#             print('- ' * 20)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'EB': 10.75,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
print(prices)

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

a = [1, 5, 2, 1, 9, 1, 5, 10]


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


print(list(dedupe(a)))

la = lambda e: e * 2
la(a)

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'), reverse=False)
print(rows_by_fname)
print(rows_by_uid)

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]  # [False, False, True, False, False, True, True, False]
print(type(more5))
print(more5)
result = list(compress(addresses, more5))
print(result)

import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
s = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(s)

import unicodedata

s = 'pýtĥöñ\fis\tawesome\r\n'
print("s: ", s)
remap = {
    ord('\t'): " ",
    ord('\f'): " ",
    ord('\r'): None
}
a = s.translate(remap)

print("a : ", a)
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(cmb_chrs)
s.format_map(vars())


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s, 20))

s = 'Elements are written as "<tag>text</tag>".'

import html

print(s)
print(html.escape(s))

int.to_bytes()
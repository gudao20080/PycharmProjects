from enum import Enum, unique


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_info(self):
        print("学习的基本信息：name = %s, age = %d" % (self.name, self.age))

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        self.score = value


@unique
class Weekly(Enum):
    Sun = 0
    Mon = 1
    Tue = 2

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return super().__str__()


import json

student = Student("WangKai", 3333)
print(json.dumps(student, default=lambda obj: obj.__dict__))

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

import os

from multiprocessing import process


def runProc(name):
    print("run child process % s, pid = %s  " % (name, os.getpid()))


print("Parent process pid = %s" % os.getpid())

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


import threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


t = threading.Thread(target=loop(), name="LoopThread")
t.start()
t.join()


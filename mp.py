#!/usr/bin/env python

from multiprocessing import Process
from time import sleep
from os import getpid, getppid
from random import random

def f():
    sleep(random())
    print getpid(), getppid()

if __name__ == '__main__':
    pool = [Process(target=f) for _ in range(10)]

    for proc in pool:
        proc.start()
    for proc in pool:
        proc.join()


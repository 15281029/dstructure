import os
import sys
from collections import Iterable

sys.path.append(os.getcwd())

from dstructure.DLink import DLink


class Queue(object):
    def __init__(self, args, length=None, default=None):
        if isinstance(args, Iterable) and length is None:
            self.__queue = DLink(args)
            self.__length = self.__queue.length
            self.__cursor = self.__queue.cursor
        elif isinstance(args, Iterable) and length > 0:
            if length < len(args):
                self.__queue = DLink([default for _ in range(length)])
                self.__length = length
                self.__cursor = self.__queue.cursor
            else:
                t = length-len(args)
                self.__queue = DLink(args)
                for _ in range(t):
                    self.__queue.append(default)
                self.__length = length
                self.__cursor = self.__queue.cursor
        elif isinstance(args, int) and args > 1:
            self.__queue = DLink([default for _ in range(args)])
            self.__length = args
            self.__cursor = self.__queue.cursor
        else:
            print("[{0}] para Error!".format(sys._getframe().f_code.co_name))

        self.display()

    @property
    def length(self):
        return self.__length

    @property
    def size(self):
        p = self.__cursor
        n = 0
        while p != None:
            if p.val is not None:
                n += 1
            p = p.next
        return n

    @property
    def isempty(self):
        if self.size <= 0:
            return True
        else:
            return False

    def display(self):
        p = self.__cursor
        while p != None:
            print('[{0}]'.format(p.val), end="")
            if p.next != None:
                print("<-->", end="")
            p = p.next
        print('')

    def enqueue(self, val):
        if self.length == 1:
            p = self.__cursor
            p.val = val
        else:
            p = self.__cursor
            for _ in range(self.length-2):
                p = p.next
            tval = p.next.val
            while p.head is not None:
                p.next.val = p.val
                p = p.head
            p.next.val = p.val
            p.val = val

        self.display()

        return tval

    def dequeue(self):
        if self.size == 0:
            print("[{0}] Queue id Empty.".format(
                sys._getframe().f_code.co_name))
            return
        else:
            p = self.__cursor
            for _ in range(self.length-1):
                p = p.next
            tval = []
            tval.append(p.val)
            while p.head is not None:
                p.val = p.head.val
                p = p.head
            p.val = None

            self.display()
            return tval

    @property
    def exit(self):
        p = self.__cursor
        for _ in range(self.length-1):
            p = p.next
        return p.val

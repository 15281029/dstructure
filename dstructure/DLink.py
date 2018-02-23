import sys
import traceback

from collections import Iterable


class LinkNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.head = None


class DLink(object):
    def __init__(self, it):
        if isinstance(it, Iterable) and len(it) > 0:
            self.__head = LinkNode(it[0])
            p = self.__head

            for i in it[1:]:
                node = LinkNode(i)
                p.next = node
                node.head = p
                p = p.next
        elif isinstance(it, Iterable) and len(it) == 0:
            self.__head = None
        else:
            print("[{0}] para Error!".format(sys._getframe().f_code.co_name))
            return

        self.cursor = self.__head
        # self.display()

    @property
    def length(self):
        p = self.__head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

    @property
    def isempty(self):
        if self.length == 0:
            return True
        else:
            return False

    def append(self, val, head=False):
        if head in [True, 'True', 'true']:
            q = LinkNode(val)
            if self.__head == None:
                self.append(val, head=False)
            else:
                p = self.__head
                self.__head = q
                self.__head.next = p
                p.head = self.__head
        elif head in [False, 'False', 'false']:
            q = LinkNode(val)
            if self.__head == None:
                self.__head = q
            else:
                p = self.__head
                while p.next != None:
                    p = p.next
                p.next = q
                q.head = p
        else:
            print("[{0}] Para Error.".format(
                sys._getframe().f_code.co_name))
            return

        called = traceback.extract_stack()[-2][2]
        if called != 'insert':
            # self.display()
            pass

    def insert(self, val, index=None):
        if self.isempty or index == None:
            self.append(val)
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return
        elif index == 0:
            q = LinkNode(val)
            q.next = self.__head
            self.__head.head = q
            self.__head = q
        else:
            p = self.__head
            for _ in range(index-1):
                p = p.next
            q = LinkNode(val)
            t = p.next
            p.next = q
            q.head = p
            q.next = t
            t.head = q
        # self.display()

    def get(self, index):
        if self.isempty:
            print("[{0}] DLink is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return
        else:
            p = self.__head
            for _ in range(index):
                p = p.next
            return p.val

    def set(self, val, index):
        if self.isempty:
            print("[{0}] DLink is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return
        else:
            p = self.__head
            for _ in range(index):
                p = p.next
            p.val = val
        # self.display()

    def display(self, reverse=False):
        if reverse in [False, 'False', 'false']:
            if self.isempty:
                print("[{0}] DLink is Empty.".format(
                    sys._getframe().f_code.co_name))
                return
            p = self.__head
            while p != None:
                print('[{0}]'.format(p.val), end="")
                if p.next != None:
                    print("<-->", end="")
                p = p.next
            print('')
        elif reverse in [True, 'True', 'true']:
            if self.isempty:
                print("[{0}] DLink is Empty.".format(
                    sys._getframe().f_code.co_name))
                return
            p = self.__head
            while p.next != None:
                p = p.next
            while p != None:
                print('[{0}]'.format(p.val), end="")
                if p.head != None:
                    print("<-->", end="")
                p = p.head
            print('')
        else:
            print("[{0}] Para Error.".format(
                sys._getframe().f_code.co_name))
            return

    def delete(self, index=None):
        if self.isempty:
            print("[{0}] DLink is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        elif index == None:
            index = self.length-1
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return

        p = self.__head
        if index == 0:
            t = p.next
            self.__head = t
            self.__head.head = None
            v = p.val
            del(p)
            # self.display()
            return(v)
        else:
            for _ in range(index-1):
                p = p.next
            q = p.next
            p.next = q.next
            q.next.head = p
            v = q.val
            del(q)
            # self.display()
            return v

    def clear(self):
        if self.isempty:
            print("[{0}] Link is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        self.__head = None

import sys
import traceback
from collections import Iterable


# 链表节点类
class LinkNode(object):
    def __init__(self, val):
        # 值域
        self.val = val
        # 指针域
        self.next = None


# 链表类
class Link(object):
    # 初始化链表
    def __init__(self, it):
        if isinstance(it, Iterable) and len(it) > 0:
            self.__head = LinkNode(it[0])
            p = self.__head

            for i in it[1:]:
                node = LinkNode(i)
                p.next = node
                p = p.next
        elif isinstance(it, Iterable) and len(it) == 0:
            self.__head = None
        else:
            print("[{0}] para Error".format(sys._getframe().f_code.co_name))
            return
        self.cursor = self.__head   # 游标操作接口
        self.display()

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

    # 在链表追加
    def append(self, val):
        if isinstance(val, Iterable):
            for i in val:
                q = LinkNode(i)
                if self.__head == None:
                    self.__head = q
                else:
                    p = self.__head
                    while p.next != None:
                        p = p.next
                    p.next = q
        else:
            q = LinkNode(val)
            if self.__head == None:
                self.__head = q
            else:
                p = self.__head
                while p.next != None:
                    p = p.next
                p.next = q

        called = traceback.extract_stack()[-2][2]
        if called != 'insert':
            self.display()

    # 获取特定节点值
    def get(self, index):
        if self.isempty:
            print("[{0}] Link is Empty.".format(
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

    # 设置特定节点值
    def set(self, val, index):
        if self.isempty:
            print("[{0}] Link is Empty.".format(
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
        self.display()

    # 显示链表
    def display(self):
        if self.isempty:
            print("[{0}] Link is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        p = self.__head
        while p != None:
            print('[{0}]'.format(p.val), end="")
            if p.next != None:
                print("-->", end="")
            p = p.next
        print('')

    # 删除特定节点
    def delete(self, index=None):
        if index == None:
            index = self.length - 1
        elif self.isempty:
            print("[{0}] Link is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return

        p = self.__head
        if index == 0:
            t = p.next
            self.__head = t
            v = p.val
            del(p)
            self.display()
            return v
        else:
            for _ in range(index-1):
                p = p.next
            q = p.next
            p.next = q.next
            v = q.val
            del(q)
            self.display()
            return v

    # 清除链表
    def clear(self):
        if self.isempty:
            print("[{0}] Link is Empty.".format(
                sys._getframe().f_code.co_name))
            return
        self.__head.next = None
        self.__head = None
        print("Link is clear!")

    # 插入节点
    def insert(self, item, index=None):
        if self.isempty or index == None:
            self.append(item)
        elif index > self.length or index < 0:
            print("[{0}] Out of Index.".format(sys._getframe().f_code.co_name))
            return
        elif index == 0:
            q = LinkNode(item)
            q.next = self.__head
            self.__head = q
        else:
            p = self.__head
            for _ in range(index-1):
                p = p.next
            q = LinkNode(item)
            t = p.next
            p.next = q
            q.next = t
        self.display()

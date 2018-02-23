from dstructure.DLink import DLink
from dstructure.Link import Link
from dstructure.Queue import Queue

# 单向链表测试
print('-'*20, '\n单向链表测试')
print('-'*20)
l = Link([i for i in reversed(range(5))])
# 在链表尾部追加元素5
l.append(5)
# 得到元素下标的元素值
print(l.get(1))
# 设置元素下标的值为4
l.set(4, 4)
# 删除最后一个元素
l.delete()
# 删除第一个元素
l.delete(0)
# 在链表尾部插入元素，等同于append
l.insert(5)
# 在链表任意部位插入
l.insert(6, 3)
# 清除整个链表
l.clear()


# 双向链表测试
print('-'*20, '\n双向链表测试')
print('-'*20)
dl = DLink([i for i in range(5)])
dl.display()
# 在链表尾部添加
dl.append(5)
dl.display()
# 在链表头部添加
dl.append(-1, head=True)
dl.display()
# 得到元素下标对应的元素值
print(dl.get(0))
# 设置元素下标对应的元素值
dl.set(-2, 0)
dl.display()
# 插入链表，不加参数index 默认为尾部
dl.insert(6)
dl.display()
# 插入链表，加index参数即为该位置
dl.insert(-3, 5)
dl.display()
# 删除元素特定下标的元素
dl.delete(0)
dl.display()
# 清除整个链表
dl.clear()
dl.display()


# 队列测试
print('-'*20, '\n队列测试')
print('-'*20)
q = Queue([i for i in range(5)])
# 进队列
for i in reversed(range(5)):
    q.enqueue(i)
# 出队列
q.dequeue()
# 得到队尾元素，没有出队列
print(q.exit)
# 得到队列长度和有效元素的个数
print(q.length, q.size)

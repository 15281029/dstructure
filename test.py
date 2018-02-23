from dstructure.DLink import DLink
from dstructure.Link import Link
from dstructure.Queue import Queue

q = Queue([i for i in range(5)])
q.dequeue()
q.enqueue(5)
print(q.enqueue(6))

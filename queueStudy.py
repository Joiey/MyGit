# import queue

class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

def hotPotato(nameList,num):
  simqueue = Queue()

  for name in nameList:
    simqueue.enqueue(name)

  while simqueue.size()>1:
    for i in range(num):
      simqueue.enqueue(simqueue.dequeue())
    simqueue.dequeue()

  return simqueue.dequeue()

print(hotPotato(['1','2','3','4','5','6'],7))
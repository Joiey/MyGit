
class node(object):
  def __init__(self,data=None):
    self.data=data
    self.next=None
  
class linked_list(object):
  def __init__(self):
    self.head = node()

  def append(self, data):
    new_node = node(data)
    current = self.head
    while current.next != None:
      current = current.next
    # insert the lastest node
    current.next = new_node
  
  def length(self):
    current = self.head
    total = 0
    while current.next != None:
      total += 1
      current = current.next
    return total
  
  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next != None:
      cur_node = cur_node.next
      elems.append(cur_node.data)
    print(elems)
  
  def getByIndex(self, index):
    if index > self.length():
      print("ERROR: index out of range")
    cur_index = 0
    cur_node = self.head
    while cur_index != index:
      cur_node = cur_node.next
      cur_index += 1
    return cur_node.data
    
  def insert(self, index, data):
    if index > self.length():
      print("ERROR: index out of range")
    new_node = node(data)
    cur_index = 0
    cur_node = self.head
    while cur_index != index:
      cur_node = cur_node.next
      cur_index +=1
    last_node = cur_node
    cur_node = cur_node.next
    last_node.next = new_node
    new_node.next = cur_node
    

my_list = linked_list()

my_list.append('John')
my_list.append('Peter')
my_list.append('Mike')
my_list.append('Alice')
my_list.append('Rose')
my_list.append('Lucy')

my_list.display()
# print(my_list.length())
# print(my_list.getByIndex(2))
my_list.insert(3,'me')
my_list.display()




class node(object):
  def __init__(self, value=None):
    self.value = value
    self.leftChild = None
    self.rightChild = None

class binarySearchTree():
  def __init__(self):
    self.root = None
  
  def insert(self, value):
    if self.root == None:
      self.root = node(value)
    else:
      self._insert(value, self.root)

  def _insert(self, value, cur_node):
    if value < cur_node.value:
      if cur_node.leftChild == None:
        cur_node.leftChild = node(value) 
      else:
        self._insert(value, cur_node.leftChild)
    elif value > cur_node.value:
      if cur_node.rightChild == None:
        cur_node.rightChild = node(value)
      else:
        self._insert(value, cur_node.rightChild)
    else:
      print(value, 'already in binary tree')

  def printTree(self):
    if self.root != None:
      self._printTree(self.root)

  def _printTree(self, cur_node):
    if cur_node != None:
      self._printTree(cur_node.leftChild)
      print(cur_node.value)
      self._printTree(cur_node.rightChild)
  
  def height(self):
    if self.root != None:
      return self._height(self.root, 0)
    else:
      return 0
  
  def _height(self, cur_node, cur_height):
    if cur_node == None:
      return cur_height
    leftHeight = self._height(cur_node.leftChild, cur_height+1)
    rightHeight = self._height(cur_node.rightChild, cur_height+1)
    return (leftHeight, rightHeight)

  def fillTree(self, elements = [13,9,14,7,10,4,8]):
    for cur_elem in elements:
      self.insert(cur_elem)
    return self

tree = binarySearchTree()
tree = tree.fillTree()
tree.printTree()
print('tree height is',tree.height())
print('root value is', tree.root.value)



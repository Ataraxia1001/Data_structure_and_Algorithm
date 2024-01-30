# 15 --> 6 --> 8

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self, data): # O(1)
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node 
      self.length += 1

  def prepend(self, data): # O(1)
    new_node = Node(data)
    new_node.next = self.head 
    self.head = new_node
    self.length += 1

  def insert(self, index, data):  # O(n)
    new_node = Node(data)
    i = 0
    cur_node = self.head
    
    if index>=self.length:
      self.append(data)
      return 
    if index ==0:
      self.prepend(data)
      return
  
    while i < self.length:
      if i == index-1:
        cur_node.next, new_node.next = new_node, cur_node.next
        self.length+=1
        break
      cur_node = cur_node.next
      i+=1
    

  def remove(self, index): # O(n)
    cur_node = self.head
    i=0
    if index>=self.length:
      print("Entered wrong index")
    
    if index == 0:
      self.head = self.head.next
      self.length -= 1   
      return       

    while i < self.length:
      if i == index-1:
        cur_node.next = cur_node.next.next
        self.length-=1
        break
      i+=1
      cur_node = cur_node.next
    
  def printl(self):  # O(n)
    cur_node = self.head
    while cur_node != None:
      print(cur_node.data , end = ' ')
      cur_node = cur_node.next
    print()
    print('Length = '+str(self.length))

  def reverse(self): # O(n)
    prev = None
    self.tail = self.head 
    
    while self.head != None:
      cur_node = self.head
      self.head = self.head.next
      cur_node.next = prev
      prev = cur_node  
    self.head = cur_node
    

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(5)
l.reverse()
l.printl()
print(l.head.data, l.tail.data)
class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def contains(self, value):
        result = False
        cur = self.head
        while cur != None:
          if cur.value == value:
            result = True
            break
          cur = cur.next
        return result

    def get_max(self):
        max = None
        cur = self.head
        while cur != None:
          if cur.value > max:
            max = cur.value
          cur = cur.next
        return max

    def add_to_tail(self, value):
      new_node = Node(value)
      if self.head == None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node 
        self.tail = new_node
      self.length += 1

    def remove_head(self):
      if self.head == None:
        return None
      else:
        if self.head == self.tail:
          self.tail = None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = LinkedList()
    self.oldest_item = None

  def append(self, item):
    if len(self.storage) == 0:
      self.oldest_item = Node(item)
      self.storage.head = self.oldest_item
      self.storage.length += 1
    elif self.capacity > len(self.storage):
      new_node = Node(item)
      node = self.storage.head
      while node:
        if node.next is None:
          node.next = Node(item)
          self.oldest_item = self.oldest_item
          self.storage.length += 1
          break
        node = node.next
    else:
      if self.oldest_item.next:
        # old = old.next
        item_to_remove = self.oldest_item
        self.oldest_item = self.oldest_item.next
        # remove old
        if item_to_remove is self.storage.head:
          new_node = Node(item)
          new_node.next = self.storage.head.next
          self.storage.head.next = None
          self.storage.head = new_node
        else:
          node = self.storage.head
          while node:
            if node.next is item_to_remove:
              new_node = Node(item)
              new_node.next = self.oldest_item
              if new_node is self.storage.head:
                self.storage.head = new_node
              else:
                node.next = new_node
              break
            node = node.next
      else:
        # find item that .next is old
        # reassign .next to new
        node = self.storage.head
        while node:
          if node.next is self.oldest_item:
            node.next = Node(item)
            self.oldest_item = self.storage.head # correct
            #self.oldest_item = self.oldest_item # NOOP!
            #self.storage.length += 1 # OOPSIES!
            break
          node = node.next

  def get(self):
    arr = []
    node = self.storage.head
    while node:
      arr.append(node.value)
      node = node.next
    return arr

buffer = RingBuffer(3)

print(buffer.get())  # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')

print(buffer.get())   # should return ['d', 'e', 'c']

buffer.append('f')

print(buffer.get())   # should return ['d', 'e', 'f']
import time
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
          if self.left is None:
            self.left = BSTNode(value)
          else:
            return self.left.insert(value)
        elif value >= self.value:
          if self.right is None:
            self.right = BSTNode(value)
          else:
            return self.right.insert(value)

    def contains(self, target):
      if self.value == target:
        return True
      if target < self.value:
        if self.left is None:
          return False
        return self.left.contains(target)
      if target > self.value:
        if self.right is None:
          return False
        return self.right.contains(target)

    def get_max(self):
      if not self.right:
        return self.value
      return self.right.get_max()

    def for_each(self, fn):
      fn(self.value)
      if self.left is not None:
        self.left.for_each(fn)
      if self.right is not None:
        self.right.for_each(fn)
      return

    def in_order_print(self, node):
      if node:
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)





start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

bst1 = BSTNode("")
for name in names_1:
  bst1.insert(name)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst2 = BSTNode("")
for name in names_2:
  bst2.insert(name)

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

def compare(x):
  if bst2.contains(x):
    duplicates.append(x)

bst1.for_each(lambda x: compare(x))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

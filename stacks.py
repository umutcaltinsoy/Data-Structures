'''

A stack is a linear data structure that stores items in a Last-In/First Out(LIFO)
or Firs-In/Last-Out(FILO) manner. In a stack, a new element is added at one end
and an element is removed from that end only. The insert and delete operations
are often called push and pop.

The functions associated with stack are:

1) empty() - Returns whether the stack s empty - Time Complexity : O(1)
2) size() - Returns the size of stack - Time Complexity : O(1)
3) top() - Returns a reference o the top most element of the stack - Time Complexity : O(1)
4) pus(g) - Adds the element 'g' at the top of the stack - Time Complexity : O(1)
5) pop() - Deletes the top most element of the stack - Time Complexity : O(1)

Implementation :
There are various ways from which a stack can be implemented in Python.
Stack in Python can be implemented using following ways :
- list
- collections.deque
- queue.LifoQueue

Implementation using list:
Python's built-in data structure list can be used as a stack. Instead of push(),
append() is used to add elements to the top of stack while pop() removes the
element in LIFO order. Unfortunately, list has a few shortcomings. The biggest
issue is that it can run into speed issue as it grows. The items in list are
stored next to each other in memory, if the stack ows bigger than the block of
memory that currently hold it, then Pythn needs to do some memory allocations.
This can lead to some append() calls taking much longer than other ones.

'''

# Here is a program to demonstrate stack implementation using list

stack = []

# append() func to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack : ', stack)

# pop() func to popo element
# from stack in LIFO order

print('\nElements poped from stack : ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nAfter elements are poped : ', stack)
# print(stack.pop()) it'll give us an IndexError!
# cause the stack is empty right now


'''

Implementation using collections.deque :
Python stack can be implmented using deque class from collections module. Deque
is preferred ove list in the cases where we need quicker append and pop operations
from both the ends of the container, as deque provides an 0(1) time complexity
for append and pop operaons as compared to list which provides O(n) time compl.
The same methods o deque as seen in list are used, appen() and pop().

'''


# Here is a program to demonstrate stack implementation
# using collections.deque

from collections import deque

stack = deque()

# append() func to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append(3)
print('Initial stack : ', stack)
print(type(stack))

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements poped from stack : ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are poped : ', stack)


'''

Implementation using queue module :
Queue module also has a LIFO Queue, which is basically a Stack. Dat is inserted
into Queue using put() function and get() takes data out from Queue.

There are various functions available in this module :

1) maxsize - Number of items allowed in the queue.

2) empty() - Return True if the queue is empty, False otherwise.

3) full() - Return True if there are maxsize items in the queue. If the queue
was initialized with maxsize=0 (the default), then full() never returns True.

4) get() - Remove and return an item from the queue. If queue is empty, wait
until an item is available.

5) get_nowait() - Return an item if one is immediately available, else raise
QueueEmpty.

6) put(item) - Put an item into the queue. If the queue is full, wait until
a free slot is available before adding the item.

7) put_nowait(item) - Put an item into the queue without blocking.

8) qsize() - Return the number of items in the queue. If no free slot is
immediately available, raise QueueFull.

'''

# Here is a program to demonstrate stack
# implementation using queue module

from queue import LifoQueue

stack = LifoQueue(maxsize = 3)

# qsize() show the number of elements in the stack
print(stack.qsize())

# put() funct. to push element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("\nFull : ", stack.full())
print("Size : ", stack.qsize())

# get() func. to pop element
# from stack in LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty :", stack.empty())


'''

Implementation using singly linked list
The linked list has two methods addHead(item) and removeHead() that run in
constant time. These two methods are suitable to implement a stack.

1) getSize() - Get the number of items in the stack.
2) isEmpty() - Return True if the stack is empty, False otherwise.
3) peek() - Return the top item in the stack. If the stack is empty, raise an exception.
4) push(value) - Push a value into the head of the stack
5) pop() - Remove and return a value in the head of the stack. If the stack is
empty, raise an exception.

'''


# Here is a program to demonstrate stack
# implementation using a linked list.
# node class

class Node:
   def __init__(self, value):
      self.value = value
      self.next = None

class Stack:

   # Initializing a stack.
   # Use a dummy node, which is
   # easier for handling edge cases.
   def __init__(self):
      self.head = Node("head")
      self.size = 0

   # String representation of the stack
   def __str__(self):
      cur = self.head.next
      out = ""
      while cur:
         out += str(cur.value) + "->"
         cur = cur.next
      return out[:-3]

   # Get the current size of the stack
   def getSize(self):
      return self.size

   # Check if the stack is empty
   def isEmpty(self):
      return self.size == 0

   # Get the top item of the stack
   def peek(self):

      # Sanitary check to see if we
      # are peeking an empty stack.
      if self.isEmpty():
         raise Exception("Peeking from an empty stack")
      return self.head.next.value

   # Push a value into the stack.
   def push(self, value):
      node = Node(value)
      node.next = self.head.next
      self.head.next = node
      self.size += 1

   # Remove a value from the stack and return.
   def pop(self):
      if self.isEmpty():
         raise Exception("Popping from an empty stack")
      remove = self.head.next
      self.head.next = self.head.next.next
      self.size -= 1
      return remove.value

# Driver Code
if __name__ == "__main__":
   stack = Stack()
   for i in range(0, 11):
      stack.push(i)
   print(f"Stack: {stack}")

   for _ in range(1, 6):
      remove = stack.pop()
      print(f"Pop: {remove}")
   print(f"Stack: {stack}")

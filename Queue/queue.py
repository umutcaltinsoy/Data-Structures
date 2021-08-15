'''

Like stack, queue is a linear data structure that stores items in
First In First Out(FIFO) manner. With a queue the least recently
added item is removed first.

Operations associated with queue are:
1) Enqueue : Adds an item to the queue. If the queue is full, then
it is said to be an Overflow condition.

2) Dequeue : Removes an item from the queue. The items are popped
in the same order in which they are pushed. If the queue is empty,
then it is said to be an Undeflow condition.

3) Front : Get the front item from queue.

4) Rear : Get the last item from queue.

Implementation  :
1- list
2- collections.deque
3- queue.Queue

'''

# Implementation using list :

'''

List is a Python's built-in data structure that can be used as a
queue. Instead of enqueue() and dequeue(), append() and pop() is
used. However, lists are quite slow for this purpose because
inserting or deleting an element at the beginning requires shifting
all of the other elements by one, requiring O(n) time.

'''

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue : ", queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)



'''

Implementation using collections.deque :
Queue can be implemented using deque class from the collections module.
Deque is preferred over list in the cases where we need quicker append
and pop operations from both the ends of container, as deque provides
an O(1) time complexity for append an pop operations as compared to list
which provides O(n) time complexity. Instead of enqueue and deque,
append() and popleft() functions are used.

'''

from collections import deque

# Inıtializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue : ", q)

# Removing elements from a queue
print("\nElements dequeued from the queue:")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)



'''

Implementation using queue.Queue :
Queue is built-in module of Python which is used to implement a queue.
Queue(maxsize) initializes a variable to a maximum size of maxsize. A
maxsize of zero '0' means a infinite queue. This Queue follows FIFO rule.

1) maxsize - Number of item allowed in the queue
2) empty() - Return True if the queue is empty, False otherwise.
3) full() - Return True if there are maxsize items in the queue.
If the queue was initialized with maxsize=0(the default, then full()
never returns True.
4) get() - Remove and return an item from the queue. If queue is empty,
wait until an item is available.
5) get_nowait() - Return an item if one is immediately available, else
raise QueueEmpty.
6) put(item) - Put an tem into the queue. If the queue is full, wait until
a free slot is available befor adding the item.
7)put_nowait(item) - Put an item into the queue without blocking. If no
free slot is immediately available, raise QueueFull.
8) qsize() - Return the number of items in the queue.

'''


from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


# Sets:

'''
A set is an unordered collection data type that is iterable,mutable
and has no duplicate elements. The major advantage of using a set,
is that it has a highly optimized method for checking whether a
specific element is contained in set. This is based on a data strc.
known as a hash table. Since sets are unordered, we cannot access
items using indexes like we do in lists.
'''

'''

#Defining a set
myset = set(["a", "b", "c"])
print(myset)
print(type(myset))

#Adding element to the set
myset.add("d")
print(myset)

'''


# Frozen Sets :

'''
Frozen sets in Python, are immutable objects that only support
methods and operators that produce a result without affecting
the frozen set or sets to which they are applied.
While elements of a set can be modified at any time, elements
of the frozen set remain the same after creation.
'''

normal_set = set(["a", "b", "c"])
print("Normal set :", normal_set)

# A frozen set
frozen_set = frozenset(["q", "w", "e"])
print("Frozen set :", frozen_set)

# If we try to add an element to a frozen set
# It'll give us an error
#frozen_set.add("x")


# Methods for Sets:


# Adding elements

name = set(["Hope", "Brave", "Jon"])
print("Name :", name, end=" ")

name.add("Zed")
print("\nNew set : ", name, end=" ")

# Adding elements to the set using iterator
for i in range(1,4):
    name.add(i)

print("\nSet after adding elements :", name, end=" ")



# Union :

'''
Two sets can be merged using union() function or | operator. Both
Hash Table values are accessed and traversed with merge operation
perform on them to combine the elements and at the same time
duplicates are removed.

'''

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union() function
population = people.union(vampires)
print("\nUnion using union() function :", population)

#Union using "|" operator
population = people|dracula

print("\nUnion using '|' operator :", population )


#Intersection :

'''
This can be done through intersection() or '&' operator. Common Elements
are selected. They are similar to iteration over the Hash lists
and combining the same values on bot the Table.
'''

set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)

for i in range(3, 9):
    set2.add(i)

# Intersection using intersection() function
set3 = set1.intersection(set2)

print("\nIntersection using intersection() function :", set3)

#Intersection using '&' operator
set4 = set1 & set2

print("\nIntersection using '&' operator :", set4)


# Difference:

'''
To find difference in between sets. Similar to fing difference in linked list.
This is done through difference() or '-' operator.
'''

s1 = set()
s2 = set()


for i in range(5):
    s1.add(i)

for i in range(3, 9):
    s2.add(i)

#Difference of two sets using difference() function
s3 = s1.difference(s2)

print("\nDifference of two sets using difference() function :", s3)

#Difference of two sets using '-' operator
s4 = s1 - s2
print("\nDifference of two sets using '-' operator :", s4)


# Clearing sets:
# Clear() method empties the whole set.

st = {1, 2, 3, 4, 5, 6}
print("Initial set :", st)

# This method will remove all the elements of the set
st.clear()
print("\nSet after using clear() function :", st)



# Code snippet to illustrate all set operations in python

# Creating two sets
a = set()
b = set()

# Adding elements to a
for i in range(1, 6):
    a.add(i)

# Adding elements to b
for i in range(3, 8):
    b.add(i)

print("a = ", a)
print("b = ", b)
print("\n")

# Union of a and b
c = a | b # a.union(b)
print("\nUnion of a & b: c = ", c)

# Intersection of a and b
d = a & b # a.intersection(b)
print("\nItersection of a & b : d = ", d)

# Checking relation between c and d
if c > d: # c.issuperset(d)
    print('c is superset of d')
elif c < d: # c.issubset(d)
    print("c is subset of d")
else: # c == d
    print("c is same as d")

# Displaying relation between d and c
if d < c: # d.issubset(c)
    print("d is subset of c")
    print("\n")

# Difference between c and d
e = c - d
print("\nElements in c and not in d: e = ", e)

# Check if d and e are disjoint sets
if d.isdisjoint(e):
    print("d and e have nothing in common\n")

# Removing all the values of e
e.clear()
print("\nAfter applying clear on sets e: e = ", e)

'''
copy()
The copy() method returns a shallow copy of the dictionary.

Syntax :
dict.copy()

Parameters :
The copy() method doesn't take any parameters.

Returns :
This method doesn't modify the original dictionary just returns copy of the
dictionary.

'''

# Example :

original = {1: 'Umut', 2: 'Cagri'}
copy = original.copy()
print("Original : ", original)
print("Copy : ", copy)


# How is it differen from simple assignment "=" ?
# Unlike copy(), the assignment operator does deep copy.

# Here is an example to demonstrate difference between "=" and cop()
original = {1: 'Zed', 2: 'Akali'}
new = original.copy()
# Removing all elements from new list and printing both
new.clear()
print("New : ", new)
print("Original : ", original)

original = {1: 'one', 2: 'two'}
# Copy using "="
new = original

# Removing all elements from new list and printing both
new.clear()
print("new  : ", new)
print("original : ", original)


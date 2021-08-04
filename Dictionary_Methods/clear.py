'''

clear()
The clear() method removes all items from the dictionary.

Syntax :
dict.clear()

Paramaters :
The clear() method doesn't take any parameters.

Returns :
The clear() method doesnt return any value.

'''

# Example :
text = {1: 'Umut', 2: 'Cagri'}
text.clear()
print("text : ", text)

'''
How is it different from assigning {} to a dictionary?
When we assign {} to a dictionary, a new empty dictionary is created and
assigned to the reference. But when we do clear on a dictionary reference,
the actual dictionary content is removed, so all references referring to
the dictionary become empty.

'''

# Here is an example to demonstrate difference clear and {}
text1 = {1: 'Zed', 2: 'Shadow'}
text2 = text1

#Using clear makes both text1 and text2 empty.
text1.clear()

print('After removing items using clear()')
print('text1 = ', text1)
print('text2 = ', text2)


text1 = {1: 'Akali', 2: 'Shuriken'}
text2 = text1

# This makes only text1 empty
text1 = {}

print('After removing items by assigning {}')
print('text1 = ', text1)
print('text2 = ', text2)




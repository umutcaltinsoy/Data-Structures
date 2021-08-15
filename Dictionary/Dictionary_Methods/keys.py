# keys()

# This method returns a view object that displays a list of all the keys
# in the dictionary in order of insertion.

# Syntax : dict.keys()


# Example :
Dictionary1 = {'A': 'Umut', 'B' : 'Cagri', 'C' : 'Altinsoy'}
print(Dictionary1.keys())

# Creating empty dictionary
empty_Dict1 = {}
print(empty_Dict1)


# Example :
# To show how updation works
Dictionary1 = {'A' : 'Umut', 'B' : 'Cagri'}
print("Keys before dictionary updation : ")
keys = Dictionary1.keys()
print(keys)

# adding an element to the dict.
Dictionary1.update({'C' : 'Altinsoy'})
print('\nAfter dictionary is updated : ', keys)
# Here, when the dictionary is updated, keys are also
# automatically updated to show the changes.


# The keys() can be used to access the elements
# of the dict as we can do for the list

# Example :
test_dict = {'Umut' : 1, 'Cagri' : 2, 'Zed' : 3}

# accessing 2nd element using loop
j = 0
for i in test_dict:
    if (j == 1):
        print('2nd key using loop : ' + i)
    j = j + 1

# accessing 2nd element using keys()
# print('2nd key using keys() : ' + test_dict.keys()[1])
# wouldn't work because python3 doesn't support indexing

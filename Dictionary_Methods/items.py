# items() method
# This method is used to return the list
# with all dict. keys with values

# Syntax : dictionary.items()
# Returns : A view object that displays a list of a given
# dictionary's (key,value) tuple pair.


# Example 1 :

Dictionary1 = { 'A' : 'Umut', 'B' : 'Cagri', 'C' : 'Altinsoy'}
print("Dictionary items :")

# Printing all the items of the Dictionary
print(Dictionary1.items())

# Example 2 : after modification

Dictionary1 = { 'A' : 'Umut', 'B' : 'Cagri'}
items = Dictionary1.items()
print("Original Dictionary items : ", items)

# Delete an item from dictionary
del[Dictionary1['B']]
print("Updated Dictionary : ", items)

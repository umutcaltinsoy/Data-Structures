# update() method

# This method updates the dictionary with the elements from the another
# dictionary object or from an iterable of key/value pairs

# Syntax : dict.update([other])
# Parameters : key-value pairs


# Example: Update with another dictionary
Dictionary1 = {'A': 'Umut', 'B' : 'Cagri'}
Dictionary2 = {'B' : 'Umut'}

# Dictionary before Update
print("Original Dictionary : ", Dictionary1)

# Update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after update : ", Dictionary1)


# Example 2 : Update with an iterable
Dictionary1 = {'A' : 'Umut'}
print("Original : ", Dictionary1)

# Update with iterable
Dictionary1.update(B = 'Cagri', C = 'Altinsoy')
print("Dictionary after update : ", Dictionary1)

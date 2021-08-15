'''
pop() method
Python language specified pop() for almost all containers, be it list, set etc.

Syntax : dict.pop(key, def)

Paramaters :
key : The key whose key-value pair has to be returned and removed.
def : The default value to return if specified key is not present.

Returns :
Value associated to deleted key-value pair, if key is present.
Default value if specified if key is not present.
KeyError, if key not present and default value not specified

'''

# Demonstrating working of pop(), when key is present.

test_dict = {"Zed" : 1, "Akali" : 2, "Amumu" : 3}
print("The dictionary before deletion : " + str(test_dict))

# Using pop to return and remove key-value pair.
pop_ele = test_dict.pop("Amumu")

# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))

# Printing dictioary after deletion:
print("Dictionary after deletion is : " + str(test_dict))


# The behavior of pop() function is different when the key is not present
# in dictionary. In this case, it returns the default provided value or
# KeyError in case even default is not provided.

# Demonstrating the working of pop() without key
test_dict = {"Zed" : 1, "Akali" : 2, "Amumu" : 3}
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair provided default
pop_ele = test_dict.pop('Jhin', 4)

# Printing the value associated to popped key prints 4
print("Value associated to popped key is : " + str(pop_ele))

# using pop to return and remove key-value pair not provided default
pop_ele = test_dict.pop('Jhin')

# Printing the value associated to popped key -- KeyError
print("Value associated to popped key is : " + str(pop_ele))

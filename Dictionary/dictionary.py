# Dictionaries :

'''
Dictionary in python is an ordered collection of data values, used to store
data values like a map, which, unlike other Data Types that hold only a
single value as an element, Dictionary holds key:value pair. Key-value is
provided in the dictionary to make it more optimized.
Key in a dictionary don't allow Polymorphism.

'''

# Creating a dictionary with integer keys
Dict = {1: 'Python', 2: 'For', 3: 'Coding'}
print(Dict)
print(type(Dict))

# Creating a dictionary with mixed keys
Dict_1 = {'Name': 'Umut', 1: [1, 2, 3, 4]}
print(Dict_1)

# Dictionary can also be created by the built-in function dict().
# An emoty dict. can be created by just placing to cury braces-{}

# Creating an empty Dictionary
d = {}
print("Empty Dictionary : ", d)

# Creating a dictionary with dict() method
dc = dict({1: 'Python', 2: 'Programming', 3: 'Umut'})
print("Dictionary with the use of dict(): ", dc)


# Nested Dictionary
# Creating a Nested Dictionary
dicts = {1: 'Umut', 2: 'Python', 3:{'A': 'Welcome', 'B': 'To', 'C': 'Programming'}}
print(dicts)
print(type(dicts))


# Adding Elements to a Dictionary

'''

One value at a time can be added to a Dictionary by defining value along
with the key e.g. Dict[Key] = 'Value'. Updating an existing value in a
Dictionary can be done by using the built-in update() method. Nested key
values can also be added to an existing Dictionary.
While adding a value, if the key value already exists, the value gets
updated otherwise a new Key with the value is added to the Dictionary.

'''

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary : ", Dict)

# Adding elements one at a time
Dict[0] = 'Umut'
Dict[2] = 'Cagri'
Dict[3] = 'Altinsoy'
Dict[4] = 1
print("Dictionary after adding 4 elements : ", Dict)

# Adding set of values to a single key
Dict['Value_set'] = 2, 3, 4
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("Updated key value : ", Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1': 'Life', '2' : 'Hard'}}
print("Adding a Nested Key : ", Dict)


# Accessing elements from a Dictionary
# In order to access the items of a dictionary refer to its key name.
# Key can be used inside square brackets.

Dict = {1: 'Python', 'name': 'Umut', 3: 'Developer'}

#accessing a element using key
print(Dict['name'])
print(Dict[1])

# There is also a method called get() that will also help in accessing the
# element from a dictionary
Dict = {1: 'Umut', 2: 'Cagri', 'Surname' : 'Altinsoy'}

# accessing an element using get()
print("Accessing an element using get : ", Dict.get('Surname'))

# Accessing element of a nested dictionary
Dict = {'Dict1': {1: 'Umut'}, 'Dict2': {'Name' : 'Cagri'}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


# Removing Elements from Dictionary

'''

Using del keyword : In python dictionary, deletion of keys can be done by
using the del keyword. Using del keyword, specific values from a dictionary
as well as whole dictionary can be deleted. Items in a Nested dictionary
can also be deleted by using del keyword and providing specific nested key
and particular key to be deleted from that nested dictionary.
del Dict will delete the entire dictionary and hence printing it after
deletion will raise an Error.

'''


Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Programming',
        'A' : {1 : 'Umut', 2 : 'Cagri', 3 : 'Altinsoy'},
        'B' : {1 : 'Zed', 2 : 'Shadow'} }

print("Inıtial Dictionary : ", Dict)

# Deleting a Key value
del Dict[6]
print("Deleting a specific key : ", Dict)

# Deleting a Key from Nested Dictionary
del Dict['A'][2]
print("Deleting a key from Nested Dictionary : ", Dict)


# Using pop() method
# Pop() method is used to return and delete the value of the key specified.
Dict = {1 : 'Zed', 2 : 'Akali', 'Skill' : 'Shuriken'}
# Deleting a key using pop() method
pop_ele = Dict.pop(2)
print("Dictionary after deletion : " + str(Dict))
print('Value associated to poped key is : ' + str(pop_ele))

# Using popitem() method
# The popitem() returns and removes an arbitrary element(key, value) pair
# from the dictionary
Dict = {1 : 'Zed', 2 : 'Akali', 'Skill' : 'Shuriken'}

#Deleting an arbitrary key using popitem() function
pop_ele = Dict.popitem()
print("Dictionary after deletion : ", str(Dict))
print("The arbitrary pair returned is : " + str(pop_ele))


# Using clear() method
# All the items from a dictionary can be deleted at once by using this method
Dict = {1 : 'Zed', 2 : 'Akali', 'Skill' : 'Shuriken'}
# Deleting entire Dictionary
Dict.clear()
print("Deleting Entire Dictionary : ", Dict)


# copy() : They copy() method returns a shallow copy of the dictionary.
# clear() : The clear() method removes all items from the dictionary.
# pop() : Removes and returns an element from a dictionary having the given key.
# popitem() : Removes the arbitrary key-value pair from the dictionary and returns it as tuple.
# get() : It is a conventional method to access a value for a key.
# dictionary_name.values() : returns a list of all the values available in a given dictionary.
# str() : Produces a printable string representation of a dictionary.
# update() : Adds dictionary dict2’s key-values pairs to dict.
# setdefault() : Set dict[key]=default if key is not already in dict.
# keys() : Returns list of dictionary dict’s keys.
# items() : Returns a list of dict’s (key, value) tuple pairs.
# has_key() : Returns true if key in dictionary dict, false otherwise.
# fromkeys() : Create a new dictionary with keys from seq and values set to value.
# type() : Returns the type of the passed variable.
# cmp() : Compares elements of both dict.

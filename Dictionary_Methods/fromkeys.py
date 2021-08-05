# fromkeys() method

# Sometimes there is a need to generate a dictionary from the given keys.
# Brute implementation of it would take time and would be more tedious job.
# Hence, fromkeys() helps us achieve this very task with ease and using
# just a single method

# Syntax : fromkeys(seq, val)
# Parameters :
# seq : The sequence to be transformed into a dictionary.
# val : Initial values that need to be assigned to the generated keys.
# Defaults to None


seq = { 'a', 'b', 'c', 'd', 'e' }

# using fromkeys() to convert sequence to dict
# initializing with None
res_dict = dict.fromkeys(seq)

# Printing created dict
print("The newly created dict with None values : " + str(res_dict))

# using fromkeys() to convert sequence to dict
# initializing with 1
res_dict2 = dict.fromkeys(seq, 1)

# Printing created dict
print("The newly created dict with 1 as value : " + str(res_dict2))


# Behaviour of fromdict() with Mutable objects as values :

seq = { 'a', 'b', 'c', 'd', 'e'}
lis1 = [2, 3]

# using fromkeys() to convert sequence to dict
# using conventional method
res_dict = dict.fromkeys(seq, lis1)

# Printing created dict :
print("The newly created dict with list values : " + str(res_dict))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append takes place in all values
print("The dict with list values after appending : " + str(res_dict))

lis1 = [2, 3]
print('\n')

# using fromkeys() to convert sequence to dict
# using dict comprehension
res_dict2 = { key : list(lis1) for key in seq }

# Printing created dict
print("The newly created dict with list values : " + str(res_dict2))

# appending to lis1
lis1.append(4)

# Printing dict after appending
# Notice that append doesnt take place now.
print("The dict with list values after appending (no change) : " + str(res_dict2))

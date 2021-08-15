'''

popitem()
Generating a random number has many application in daily life. In a list,
various functions are supported for the same. A whole library is dedicated
in Python to hadnle random numbers. But sometimes, we need to perform a
similar task with a dictionary. popitem() method in dictionary helps to
achieve similar purpose. It removes the arbitrary key-value pair from the
dictionary and return it as a tuple.

Syntax : dict.popitem()
Parameters : None
Returns : A tuple containing the arbitrary key-value pair from dictionary.
That pair is removed from dictionary.

'''

# Demonstrating the use of popitem()
test_dict = {"Zed" : 1, "Akali" : 2, "Jhin" : 3}
print("The dictionary before deletion : " + str(test_dict))

# using popitem() to return and remove arbitrary pair
res = test_dict.popitem()

# Printing the pair returned
print("The arbitrary pair returned is : " + str(res))

# Printing dictionary after deletion
print("The dictionary after removal" + str(test_dict))

# This particular function can be used to formulated the random name for
# playing a game or deciding the random ranklist without using any random
# function.


# Demonstrating application of popitem()
test_dict = {"Zed" : 1, "Akali" : 2, "Jhin" : 3, "Master Yi" : 4, "Rammus" : 5}
print("The dictionary before deletion : " + str(test_dict))

n = len(test_dict)

# using popitem to assign ranks
for i in range(0, n):
    print("Rank" + str(i + 1) + " " + str(test_dict.popitem()))

# Printing end dict
print("The dictionary after deletion : " + str(test_dict))

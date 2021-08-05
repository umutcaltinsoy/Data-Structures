'''

values()

values() is an inbuilt method in Python that returns a list of all the
values available in a given dictionary.

Syntax : dictionary_name.values()

Paramaters : There are no parameters.

Returns : Returns a list of all the values available in a given dictionary.
The values have been stored in a reversed manner.

'''

# Example 1:

# numerical values
dictionary = {"Umut" : 1, "Cagri" : 2, "Zed" : 3}
print(dictionary.values())

# string values
dictionary = {"Umut" : "1", "Cagri" : "2", "Zed" : "3"}
print(dictionary.values())


# Example 2 : Given character and damage, return the total damage of all characters.
damage = {"Zed" : 1000, "Akali" : 500, "Urgot" : 1000}

# stores the damages only
damage_list = damage.values()
print(sum(damage_list)) # prints the sum of all damages

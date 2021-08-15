# get() method

# In python dictionaries, following is a conventional method to access a
# value for a key.

dic = {"A":1, "B":2}
print(dic["A"])
# print(dic["C"]) it'll give us a KeyError!

# The get() method is used to avoid such situations. This method returns
# the value for the given key, if present in the dictionary. If not, then
# it'll return 'None' (if get() is used with only one argument).

# Syntax
# Dict.get(key, default=None)

# Here is an example :
dic = {"A":1 , "B":2}
print(dic.get("A"))
print(dic.get("C"))
print(dic.get("C", "Not Found! "))

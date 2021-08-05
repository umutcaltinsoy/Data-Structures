# type()

# Example 1 :
print(type([]) is list)
print(type([]) is not list)
print(type(()) is tuple)
print(type({}) is dict)
print(type({}) is not list)


# Example 2 :
# Class of type dict
class DictType:
    DictNumber = {1 : 'Umut', 2 : 'Cagri',
                3 : 'Zed', 4 : 'Akali'}

    # will print the object type
    # of existing class
    print(type(DictNumber))
# Class of type list
class ListType:
    ListNumber = [1, 2, 3, 4, 5, 6]
    print(type(ListNumber))

# Class of type tuple
class TupleType:
    TupleNumber = ('Zed', 'Akali', 'Teemo')
    print(type(TupleNumber))


# Example 3 :
# Class of type dict
class DictType:
    DictNumber = {1 : 'John', 2 : 'Wick', 3 : 'Scarlett', 4 : 'Johansson'}

# Class of type list
class ListType:
    ListNumber = [1, 2, 3, 4, 5]

# Creating object of each class
d = DictType()
l = ListType()

# Will print accordingly whether both
# the objects are of same type or not
if type(d) is not type(l):
    print("Both class have different object type. ")
else :
    print("Sme object type. ")


new = type('New', (object, ), dict(var1 = 'UmutCagri', b = 2021))
print(type(new))
print(vars(new))

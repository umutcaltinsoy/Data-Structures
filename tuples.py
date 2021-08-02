#Tuples :
#Tuple is a sequence type just like lists, but it is immutable.
#A tuple consists of a number of values separated by commas.
'''
#Creating Tuples:
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

a = (1, 2, 3)
print(a[0])
print(type(a))

#Another way to creating tuple
tup = 'python', 'data'
print(tup)
print(type(tup))

#tup_2 = ('python', 'data')
#print(tup_2)
#print(type(tup_2))

'''


'''
#The enclosing braces are optional.
a = 1, 2, 3
print(a[0])
print(type(a))


#The built-in function len and slicing works on tuples too.
print(len(a))
print(a[0:])

#Tuples with a single value are represented with an additional comma.
b = (1,)
print(type(b))
'''


'''
#Concatenation of Tuples:
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'data')

print(tuple1 + tuple2)
'''

'''
#Nesting of Tuples:
#Using tuple1 and tuple2
tuple3 = (tuple1, tuple2)
print(tuple3)

#Repetition in Tuples:
tuple4 = ('python',)*3
print(tuple4)
'''

#Immutable Tuples:
#t = (0, 1, 2, 3)
#t[0] = 4
#print(t) #It'll give us TypeError!


'''
#Slicing in Tuples:
tuple1 = (0, 1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
'''


'''
#Deleting a Tuple:
t = (1, 2)
del t
print(t) #It'll give us a NameError!
'''


'''
#Finding length of a Tuple:
tuple2 = ('python', 'data')
print(len(tuple2))
'''


'''
#Converting list to a Tuple:
list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python')) #String 'python'
'''


'''
#Tuples in a loop:
tup = ('data',)
n = 5 #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)
'''


'''
#Here is an example: Using cmp(), max(), min()

#A python program to demonstrate the use of
#cmp(), max(), min()

tuple1 = ('python', 'data')
tuple2 = ('coder', 'developer')

#cmp() doesn't exist in python3. We must define ourselves
def cmp(a, b):
    return (a > b) - (a < b)


if (cmp(tuple1, tuple2) != 0):
    #cmp() returns 0 if matched
    print('Not the same')

else:
    print('Same')
print('Maximum element in tuples 1,2:' +
        str(max(tuple1)) + ',' +
        str(max(tuple2)))
print('Minimum element in tuples 1,2:' +
        str(min(tuple1) + ',' +
        str(min(tuple2))))
'''

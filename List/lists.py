'''
#Lists

#Defining a basic list:
list = [1, 2, 3, 4]
print(type(list))

#A List contain another list as member:
a = [1, 2, 3]
b = [1.5, 2, 4, a]
print(b)
print(type(b))
print(type(b[3])) #We can access a specific compenent's type as well.

print(len(a)) #The built-in function 'len' can be used to find the length of a list.

#The '+' and '*' operators work on even lists.
a = [1, 2, 3]
b = [4, 5]
print(a+b)
print(b*3)


#List can be indexed to get individual entries.
a = [1, 2, 3]
print(a[0])

#When a wrong index is used, python gives an error.
#list = [1, 2, 3, 4]
#print(x[4]) Error!

#Negative indices can be used to index the list from right.
list = [1, 2, 3, 4]
print(list[-1])
print(list[-3])


#We can use list slicing to get part of list.
list = [1, 2, 3, 4]
print(list[0:2]) #Not included 2
print(list[0:]) #From 0th to end(whole indices)
print(list[0:-1]) #Also using for negative indices
print(list[:]) #Whole indices


#An optional third index can be used to specify the increment.
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x[0:6:2])
print(x[::-1]) #We can reverse a list, just by providing -1 for increment.


#List members can be modified by assignment.
list = [1, 2, 3, 4]
list[0] = 9
print(list)

#Presence of a key in a list can be tested using 'in' operator. It'll return True/False.
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(2 in x)


#Values can be appended to a list by calling 'append' method on list.
ls = [1, 2, 3]
ls.append(4)
print(ls)

#Here is an example: What will be the output of the following program?
#k = [0, 1, [2]]
#k[2][0] = 3
#print(k)
#k[2].append(4)
#print(k)
#k[2] = 2
#print(k)

'''


'''

#For Statement:
#Python provides 'for' statement to iterate over a list.

for x in [1, 2, 3, 4]:
    print(x)
for i in range(10):
    print(i, i**2, i*i*i)

#The built-in function 'zip' takes two lists and returns list of pairs.
name = ['Mark', 'Alice', 'Jon']
age = [21, 22, 42]
z = list(zip(name,age))
print(z)

#It is hand when we want to iterate over two lists together.
names = ["a", "b", "c"]
value = [1, 2, 3]
for names,value in zip(names, value):
    print(names, value)

'''

'''
#Sorting Lists:
#The 'sort' method sorts a list in place.
list = [132, 12, 21, 1, 1323]
list.sort()
print(list)

#The built-in function 'sorted' returns a new  sorted list without modifying the source list.
a = [3, 2, 1, 4, 5, 6]
a.sort()
print(a)


#Example: Write a function 'lensort' to sort a list of strings based on length.
ls = ['python', 'perl', 'java', 'c', 'ruby', 'haskell']
def Sorting(ls):
    ls2 = sorted(ls, key=len)
    return ls2
print(Sorting(ls))
'''

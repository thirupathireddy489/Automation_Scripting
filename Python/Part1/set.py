# set - {} - not important for real-time
##############################################
# set is a sequence of objects in {}
# set not allows duplicates
# set has no order
# no indexing
# no +, no *
# set is mutable - will show using methods
# set methods:
#   add,remove,pop,copy,clear,update


data = {10, 30, "india", "uk", "india", 30, 30, "uk"}
print(data)
#No duplicates - {10, 'uk', 'india', 30}

data = {10, 30, "india", "uk", "india", 30, 30, "uk"}
print(data[0])
#TypeError: 'set' object is not subscriptable


set1 = {11,22,33}
set2 = {44,55,66}
set3 = set1 + set2
print(set3)
#TypeError: unsupported operand type(s) for +: 'set' and 'set'


set1 = {11,22,33}
ouut = set1 * 4
print(ouut)
#TypeError: unsupported operand type(s) for *: 'set' and 'int'


# add - used to add ONE object at random place
# if object already exists, then it will not add
data = {"india", "uk", "germany"}
print(data)
data.add(100)
data.add("usa")
data.add("uk")
print(data)


# remove - used to remove a object from set
data = {"india", "uk", "germany"}
print(data)
data.remove("uk")
print(data)


# pop - randomly removes an object
data = {"india", "uk", "germany", "japan", "usa"}
out = data.pop()
print(data)
print(out)


# pop - cant pass argument to set pop - error
data = {"india", "uk", "germany", "japan", "usa"}
out = data.pop("uk")
print(data)
#TypeError: set.pop() takes no arguments (1 given)



# copy - used to copy one set into another
data = {"india", "uk", "germany"}
temp = data.copy()
print(data)
print(temp)


# clear - used to clear/empty the set
data = {"india", "uk", "germany"}
print(data)
data.clear()
print(data)

# below syntax to define empty set
temp = set()


# create empty set and add object/element to set#se
temp = set()
print(temp)
temp.add(10)
print(temp)
print( type(temp) )



# update - used to add MULTIPLE objects to set
####################################################
data = {"india", "uk", "germany"}
data.update( [10, 20, 30] )
print(data)
#{'uk', 'india', 10, 20, 'germany', 30}

data.update( {10, 20, 30} )
print(data)
#{'uk', 'india', 10, 20, 'germany', 30}

data.update( (10, 20, 30) )
print(data)
#{'uk', 'india', 10, 20, 'germany', 30}

data.update( {10:1, 20:2, 30:3} )
print(data)
#{'uk', 'india', 10, 20, 'germany', 30}
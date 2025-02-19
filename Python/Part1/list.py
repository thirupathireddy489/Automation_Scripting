# list
#   used for storing multiple objects of any type in []
#   supports concatination +
#   supports repetition *
#   list allowes duplicates
#   list has order
#   list supports indexing, -ve or +ve
#   list is mutable - possible to update object in-place
#   list methods:
#       append,insert,extend,remove,pop,index,count
#       update,copy,clear,reverse

data = [100, 3.5, "india", 100, 100, 20, 20, "india"]
print(data)

# + - concatination
data = [100, 3.5, "india", 100, 100, 20, 20, "india"]
print(data + data)

# * - repetition
data = [100, 3.5, "india", 100, 100, 20, 20, "india"]
print(data * 3)

#how to access object/element from the list
#using index
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", "100"]
print(data[2])
print(data[-2])

#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
print(data[-1])

#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
# we can update list data in-place --> mutable
# important
data[2] = 1000
print(data)

# str - immutable - we can not update same str
data = "abc"
print(data)
#data[1] = "m" #TypeError: 'str' object does not support item assignment
print(data)

# str - immutable - we can not update same str
data = "abc"
out = data.replace("b", "m")
print(data)
print("*********************")
print(out)

# append - used to add ONE object to end of list
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.append(100)
data.append(200)
print(data)

# insert - used to insert ONE object using index/postion
# list.insert(index, OBJECT)
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.insert(2, "japan")
print(data)
"""

#          0       1       2         3       4        5
data = ["india", "uk", "japan", "germany", "japan", True]
"""

# insert - used to insert ONE object using index/postion
# list.insert(index, OBJECT)
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.insert(0, 100)
print(data)


#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.insert(-2, 50)
print(data)


# remove - used to remove OBJECT from list
# list.remove(OBJECT)
# if OBJECT does not exist - error
# if there multiple OBJECT, removes ONLY first occurances
# how to remove all occurances - learnt in loops
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.remove("germany")
print(data)
data.remove("JAPAN")


#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", "germany"]
print(data)
out = data.remove("germany")
print(data)
print("************************")
print(out)


# pop - used to remove object but using index
# used to remove index
# list.pop(index)
# index can be -ve or +ve
# if index does not exist - error
#          0       1       2         3       4
data = ["india", "uk", "germany", "japan", True]
print(data)
data.pop(2)
print(data)
data.pop(9)


#if you want to know the which object we have removed - we can that removed get value
data = [3434,45345,45,535,4354,654,6454,324,23,2,3,44,65,7,657,568,523,23,43,5,46,57,657,657,56,78,56,3454,3,2,31,4,36,456,]
print(data)
out = data.pop(19)
print(data)
print("*******************************************")
print(out)


# count - used to get count of specific object
#          0       1       2         3       4    5        6
data = ["india", "uk", "germany", "japan", "uk", "uk", "ukraine"]
out = data.count("uk")
print(out)


data = ["india", "uk", "germany", "japan", "uk", "uk", "ukraine"]
out = data.count(data[5])
print(out)


# dict {k1:v1, k2:v2} - dictionary --> very very important
###################################################
# dict is sequence of key and value pairs
# key should be uniq, if duplicate we will get value of later one
# value can be anything - duplicates allowed
# key must be ONLY immutable - int/float/str/tuple/bool
# no support for indexing
# dict is mutable - we can update
#    shown how to update and insertb - very important
# no +, no *
# dict methods:
#    keys,values,items,pop,popitem,update,copy,clear

# bool True  --> 1
# bool False --> 0

##          
#data = ["india", "uk", "germany", "uk", "uk"]

#        ad123     ad345    ad111
data = ["ramesh", "kiran", "vijay"]



"""
fast:    --> speed ...
coin:    --> money, round shaped object
"""


temp = ["india", "uk", "germany"]
data = {2: "india", 5: "uk", 8: "germany"}
print(data)


data = {2: "india", 5: "uk", 8: "germany", 9: "uk", 2: "usa"}
print(data)


data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 2.5: 10, True: "ab"}
print(data)


temp = ["ramesh", "kiran", "vijay"]
print(temp[1])
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
# how to get value for a specific key?
# how to get specific value from dict?
# how to access/get data from dict?
print(data["rn4"])
print(data[25])
# print(data[0])


# temp = ["ramesh", "kiran", "vijay"]
# # how to update list?
# temp[1] = "rahul"
### below will not work
# temp[3] = "rahul"
# how to update dict? - very important
# dict[EXISTING_KEY] = VALUE
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
print(data)
data["rn4"] = "rahul"
print(data)


# how to insert into dict? - very important
# dict[NEW_KEY] = VALUE
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
print(data)
data["rn5"] = "rahul"
print(data)

x = {11:22}
y = {33:44}
out = x + y
print(out)
#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

x = {11:22}
out = x * 5
print(out)
#TypeError: unsupported operand type(s) for *: 'dict' and 'int'

# keys - used to get all keys from dict
#########################################################################
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
out = data.keys()
print(out)
print(type(out))
print(type(data))


#type() - it is inbuilt function. it will give you the which data type it is
no = 10
print(type(no))


# values - used to get all values from dict
#########################################################################
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
out = data.values()
print(out)


# items - to get all key and values
############################################################
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay", 25: "india"}
out = data.items()
print(out)


# update - used to insert/update dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
# data[10] = 20
data.update(rn4="rahul", rn1=500, rn6="laxman")
print(data)


# update - used to insert/update dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
# data[10] = 20
data.update({"rn4":"rahul", "rn1":500, "rn6":"laxman", 10:20})
print(data)
#{'rn1': 500, 'rn4': 'rahul', 'rn8': 'vijay', 'rn6': 'laxman', 10: 20}

# update - used to insert/update dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
data2 = {"rn4":"rahul", "rn1":500, "rn6":"laxman", 10:20}
data.update(data2)
print(data)
#{'rn1': 500, 'rn4': 'rahul', 'rn8': 'vijay', 'rn6': 'laxman', 10: 20}


# data.pop(1)
# pop - used for removing key from dict..
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
data.pop("rn4")
print(data)


# pop - used for removing key from dict..
#store removed key in the variable
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
out = data.pop("rn4")
print(data)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(out)
print(type(out))
#kiran

#try to remove not existing key from the dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
out = data.pop("rn10")
print(data)
#KeyError: 'rn10'

#pop will expect at least ONE argument - pop(KEY)
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
out = data.pop()
print(data)
#TypeError: pop expected at least 1 argument, got 0


# popitem - used to remove last item from dict
#####################################################
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
data.popitem()
print(data)


# popitem - used to remove last item from dict
#####################################################
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
out = data.popitem()
print(data)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(out)
print(type(out))
#('rn8', 'vijay')
#<class 'tuple'>


# clear - used to clear the dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
print(data)
data.clear()
print(data)


# copy - used to copy one dict into another dict
data = {"rn1": "ramesh", "rn4": "kiran", "rn8": "vijay"}
temp = data.copy()
print(data)
print(temp)



# declare empty dict
data = {}

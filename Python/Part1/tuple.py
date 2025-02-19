# tuple - () - not used by developer in real-time
# tuple is sequence of multiple ANY object
# supports concatenation using +
# use * for repeatation
# supports indexing -ve/+ve
# allows duplicates
# tuple has order
# tuple is immutable - we can not update
# tuple methods
#    index, count


data = (10, 20, 30)
print(data)
data[0] = 500
print(data)
#TypeError: 'tuple' object does not support item assignment


# total uk?
# count - used to get count of a specific object
data = ("india", "uk", "germany", "uk", "uk")
out = data.count("uk")
print(out)

out = data.count("germany")
print(out)


# index - used to get index/position object..
#         0        1       2       3     4
data = ("india", "uk", "germany", "uk", "uk")
out = data.index("germany")
print(out)

out = data.index("uk")
print(out)

out = data.index("ger")
print(out)
#ValueError: tuple.index(x): x not in tuple
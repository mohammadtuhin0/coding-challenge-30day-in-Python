# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets cannot have two items with the same value.


thisset = {"apple", "banana", "cherry"}
print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))



# Set Items - Data Types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


# Python - Access Set Items:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  
# Python - Add Set Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Python - Remove Set Items:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)



# Python - Loop Sets:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  
# Join Multiple Sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# Intersection:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


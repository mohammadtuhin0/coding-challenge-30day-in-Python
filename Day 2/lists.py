thislist = ["Apple", "Banana", "Cherry"]
print(thislist)

# List Length
thislist = ["Orange", "Mango", "Python", "SQL"]
print(len(thislist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list
thislist = list(("apple", "banana", "cherry"))
print(thislist)


# Python - Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Range of Indexes:
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])        #[start:end]


# Check if Item Exists:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list");
else:
    print("No, apple is not the fruits list");
    
    
    
# Python - Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Insert Items
# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# Append Items:
# To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Remove Specified Item:
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Loop Through a List:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
# List Comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
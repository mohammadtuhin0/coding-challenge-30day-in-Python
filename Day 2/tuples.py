thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Range of Indexes:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# Python - Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Python - Loop Tuples:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  
#   Using a While Loop:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
  

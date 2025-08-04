# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello World!"
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# String Length
a = "Mohammad Tuhin!"
print(len(a))

# Check String
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  

# Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Python - Modify Strings
a = "Hello, World!"
print(a.upper())                # upper() method

a = "Hello, World!"
print(a.lower())                # lower() method

a = "Hello, World!"
print(a.replace("H", "J"))      # replace() method


# Python - Format - Strings
age = 36
txt = "My name is John, I am " + age
print(txt)

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
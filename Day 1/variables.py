# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


x = 5           # x is type int
y = "John"      # y is now of type str
print(x)
print(y)


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


myVariableName = "John"             # Camel Case
myVariableName = "John"             # Pascal Case
my_variable_name = "John"           # Snake Case


a = "Python"
b = "is"
c = "awesome"
print(a + b + c)

# Global Variables
x = "awesome"

def myfunction():
    print("Pyhton is " + x)
myfunction()
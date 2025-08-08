# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
    print("Hello from a function.")
my_function()


# Arguments
def my_function(fname):
    print(fname + " Refsnes")
    
my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Mohammad", "Tuhin")


# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[0])
my_function("Tasin", "Ayat", "Tabassum")


# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results: ")
tri_recursion(7)
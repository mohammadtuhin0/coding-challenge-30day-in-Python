# ✅ variables.py

# Take two integer inputs and print their sum, difference, and product.
x = 12
y = 8
sum = x + y
difference = x - y
product = x * y
print(sum, difference, product)

# Combine a number with a fixed string and print it like: "Number is 5".
number = 5
print("Number is " + str(number))


# ✅ syntax.py

# Find the error in this code and explain why it happens:
            # if 5 > 2
            #     print("ok")
if 5 > 2:
    print("ok")
#  Explanation:
# In Python, every if statement must end with a colon (:).
# Without the colon, Python gives a SyntaxError.



# ✅ strings.py
# Take a string from the user and print it reversed.
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string: ", reversed_text)
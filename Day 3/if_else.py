a = 33
b = 199
if b > a:
    print("B is greater than a")
    
    
# Elif
a = 33
b = 33
if b > a:
    print("B is greater than a ")
elif a == b:
    print("A and B are equal")
    

# Else
a = 150
b = 50
if a < b:
    print("B is greater than a")
elif a == b:
    print("A and B are equal")
else:
    print("A is greater than B")
    
    
    
# Nested If
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("But not above 20.")
# For Loop Problems:

# Problem : Calculate the sum of numbers from 1 to 50.
total = 0
for i in range(1,51):
    total += i
print("The sum is: ", total)


# Problem : Print all even numbers from 1 to 20.
for i in range(1,21):
    if i % 2 ==0:
        print(i)


# If-Else Problems:

# Problem : Take a number from the user. Print "Even" if it’s even, otherwise print "Odd".
number = int(input("Enter the number: "))
if number % 2 ==0:
    print("Even")
else:
    print("Odd")
    
    
# Match-Case Problems:

# Problem : Take a number (1–7) as input. Use match-case to print the corresponding day of the week.
day = int(input("Enter a number(1-7):"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")
     
     
# While Loop Problems:

# Problem : Take a number from the user and keep printing "love" until that many times.
code_string = '''
i = 1
while True:
    print(i, "love")
    i += 1
'''

exec(code_string)
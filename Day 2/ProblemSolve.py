# lists problem solve

# Problem 1: Take 5 integers from the user and store them in a list. Then print the sum and average.
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
total = sum(numbers)
average = total / len(numbers)

print("Numbers entered: ", numbers)
print("Sum:", total)
print("Average: ", average)



# Tuples
# Problem :Create a tuple with 5 elements and print the first and last elements.

my_tuple = (10, 20, 30, 40, 50)
print("First element: ", my_tuple[0])
print("Last element:", my_tuple[-1])



#  Sets
# Problem :Create two sets and find:
# The union
# The intersection
# The difference
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_result = set1.union(set2)
intersection_result = set1.intersection(set2)

difference_result = set1.difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference (set1 - set2):", difference_result)



#  Dictionaries
# Problem :
# Create a dictionary with 3 students and their marks. Then:

# Print all keys and values.

# Find the student with the highest marks.
# Create dictionary with students and their marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Students and their marks:")
for name, marks in students.items():
    print(name, ":", marks)

top_student = max(students, key=students.get)
print("Top student:", top_student)
print("Highest marks:", students[top_student])

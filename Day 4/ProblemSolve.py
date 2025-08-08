# Problem 1: Find the Maximum Number

def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
numbers = [10,45,3,77,32]
print("Maximum number:", find_max(numbers))

# Problem 2: Sum of Even Numbers
def sum_even_numbers(arr):
    total = 0
    for num in arr:
        if num % 2 ==0:
            total += num
    return total
numbers = [1,2,3,4,5,6]
print("Sum of even numbers: ", sum_even_numbers(numbers))

# Problem 3: Reverse a List

def reverse_list(arr):
    return arr[::-1]
my_list = [1,2,3,4,5]
print("Reversed List: ", reverse_list(my_list))
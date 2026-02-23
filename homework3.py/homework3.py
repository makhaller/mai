#3.1 Say Goodbye
def say_hello(name):
    print("Hello,", name)
name = "Mai"
say_hello(name)

def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye(name)

#3.2 Area of a Circle
def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius 
    print(area)
(circle_area(5))

#4.1 Subtract, Multiply, and Divide 
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b 

print(add(2, 1))
print(subtract(16, 19))
print(multiply(28, 0.125))
print(divide(16, 5))

#5.1 What Should I wear?
def get_min_max(temps):
    return (min(temps), max(temps))
readings = [15, 14, 17, 20, 23, 28, 20]
result = get_min_max(readings)
print(result)

def what_should_i_wear(temps):
    low, high = get_min_max(temps)

    if high >= 25:
        return "It's hot - wear crop top and jeans"
    elif low <= 10:
        return "It's cold - wear a sweater and cargo pants"
    else:
        return "The weather is mild - take the gamble"
    
print(get_min_max(readings))
print(what_should_i_wear(readings))

#5.2 Check if it's the Weekend 
def is_weekend(day):
    if day == "Saturday" or day == "Sunday":
        return "It's the weekend! :)"
    else: 
        return "It's not the weekend. :("
    
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False 

print(is_weekend(6))
print(is_weekend(3))
print(is_weekend(7))

#5.3 Fuel Efficiency Calculator 
def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used

print(fuel_efficiency(300, 10))
print(fuel_efficiency(450, 15))
print(fuel_efficiency(500,20))

#5.4 Secret Code 
def secret_code(n):
    last_digit = n % 10
    rest = n // 10
    digits = len(str(rest))
    return last_digit * (10 ** digits) + rest

print(secret_code(12345))
print(secret_code(4290))

#6.1 Oski Stole Your Power 
def power(x, y):
    result = 1
    for _ in range(y):
        result = result * x 
    return result 

print(power(2, 4))
print(power(5, 5))
print(power(215, 0))

#6.2.1 For Loops
def find_min(nums):
    smallest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
    return smallest 
def find_max(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest 

numbers = [15, 14, 17, 20, 23, 28, 20]
print(find_min(numbers))
print(find_max(numbers))

#6.2.2 While Loops
def find_min_while(nums):
    smallest = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] < smallest:
            smallest = nums[i]
        i += 1
    return smallest 
def find_max_while(nums):
    largest = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > largest:
            largest = nums[i]
        i += 1
    return largest 

numbers = [15, 14, 17, 20, 23, 28, 20]
print(find_min_while(numbers))
print(find_max_while(numbers))

#6.3 Calculator the Sun 
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total 

print(sum_digits(2468))
print(sum_digits(12345))

#7.1 In Your VS Code Terminal 
number = 12345
result = secret_code(number)
print(f"The result of Secret Code (5.4) with input {number} is {result}.")
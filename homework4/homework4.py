#3.1 List Operations
foods = ["sushi", "poke", "cheeseburger", "pasta", "thai"]

print(foods[1]) #second food
print(foods[-1]) #last food 

foods.append("ramen") #add new food to end 
foods.insert(0, "apple") #insert apple at start 

del foods[2] #removw third item

print(len(foods)) #length of list 

for food in foods: 
    print(food.upper()) #loop and print uppercase

first_and_last = [foods[0], foods[-1]] #new list with first and last 
print(first_and_last)

if "potato" in foods:
    print("A potato!")
else: 
    print("No potato!")

#3.2 Slicing and Striding 
numbers = list(range(21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)

#3.3.1 Nested List Operations
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers =[
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])
numbers.append([10, 11, 12])

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total 

print(sum_nested(numbers))

#3.4 Create a 5x5 List
def create_5x5():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

def replace_multiples_of_3(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for value in row:
            if value % 3 == 0:
                new_row.append("?")
            else: 
                new_row.append(value)
        new_grid.append(new_row)
    return new_grid

def sum_not_question(grid):
    total = 0
    for row in grid: 
        for value in row:
            if value != "?":
                total += value
    return total 

original_5x5 = create_5x5()
updated_5x5 = replace_multiples_of_3(original_5x5)
final_sum = sum_not_question(updated_5x5)

print(original_5x5)
print(updated_5x5)
print(final_sum)

#4.1 Dictionary Operations 
ages = {
    "Katie": 30, 
    "Mariam": 42, 
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100 
ages["Milana"] = 52 
del ages["Mariam"]

for name, age in ages.items():
    print(name, age)

#5.1
print(sum_not_question(updated_5x5))

# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals 

b=1.5 
print(b)
print(type(b)) #b is an float, a number with a decimal 

c = 3j
print(c)
print(type(c)) #c is a complex number, has both a real and an imaginary part 

d = "hello"
print(d)
print(type(d)) #d is a string, has text

e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, collection of items 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, holds labeled values

g = (1,2)
print(g)
print(type(g)) #g is a tuple, values that cannot be changed 

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list, values that you can change 

i = True
print(i)
print(type(i)) #i is a boolean, value that is either true or false 

j = None
print(j)
print(type(j)) #j is a nonetype, has no value 

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list, values that you can change

l = str(14)
print(l)
print(type(l)) #l is a string, has text

m = 1e4 
print(m)
print(type(m)) #m is a float, a number with a decimal 

#Questions and Answers:
#How many differnet data types did you find? --> 9
#List all the data types you found --> integer, float, complex, string, list, dict, tuple, boot, nonetype
#What variables have the same data types? --> b and m are the same, d and l are the same, e h and k are the same
#What was the data type of l? Why is it not an integer? What does str() do? --> l is a string, it is not an integer because it converts into a string using the str() command, which turns soemthing into text 
#Look up one more data type not given above. Repeat the same procedure 
n = {1, 2, 3}
print(n)
print(type(n)) #n is a set, a collection of unique values

print(10>9) #True, 10 is greater than 9
print (10==9) #False, 10 is not equal to 9
print(10<=9) #False, 10 is not less than or equal to 9
bool("abc")
print(bool("abc")) #True, because it's not false
bool(123)
print(bool(123)) #True, because it's not false
bool(["apple", "cherry", "banana"])
print(bool(["apple", "cherry", "banana"])) #True, because it's not false 
bool(True)
print(bool(True)) #True, because it's not false 
bool(False)
print(bool(False)) #False, because it's not true 
bool(0)
print(bool(0)) #False, because 0 is a false value 
bool("")
print(bool("")) #False, because there is nothing in it (empty)
bool(" ")
print(bool(" ")) #True, because there is a space in it 
bool(())
print(bool(())) #False, it is empty
bool([])
print(bool([])) #False, it is empty 
bool({})
print(bool({})) #False, it is empty 
bool(True and False)
print(bool(True and False)) #False, because you cannot have true and false to be true, so its false (both statements have to be true or false)
bool(True and True)
print(bool(True and True)) #True, becuase both are true 
bool(False and False)
print(bool(False and False)) #False, because both are false
bool(True or False)
print(bool(True or False)) #True, because only one condiiton is true for the entire statement to be true
bool(True or True)
print(bool(True or True)) #True, because only one condition needs to be true for the entire statement to be true
bool(False or False)
print(bool(False or False)) #False, becuase only one condiotn needs to be false for the entire statement to be false
bool(not(False)) 
print(bool(not(False))) #True, because not false is true
bool(not(True))
print(bool(not(True))) #False, because not true is false 

#Questions and Answers:
#What patterns do you notice about expressions turning True or False? --> some of the true of false statements are more logical, like 9>10 being false, because mathematically that is simply not true
#But in other statements, like the and/or statements, relies also on somne logical reasoning but some have a pre-set condition to be True, like True or False being True
#Which expression surprised you about its result? --> The bool(True or False) statement being true, and not both. I don't think being both is a possibility, 
#but I found it weird that is it automatically true, I think I need to detach the literal english meaning from these terms and understand them more in a CS lens 
#Create an expression, not given above, that will return True. Why is it True?
mare = "female horse"
print(mare == "female horse") #True because it's a string that is equal (==) to its definiton
#Create an expression, not given above, that will return False. Why is it false?
Manchild = "stupid, useless, slow"
print(Manchild=="smart and cool") #False because the string does not match the defintion (Thank you Sabrina Carpenter)

print(10+5) #15, + performs addition 
print(10-5) #5, - performs subtraction
print(2*4) #8, * performs multiplication 
print(6/3) #2, % performs division 
print(3**2) #9, performs exponent operation 
print(15//2) #7, performs division but rounds down to the nearest whole number 
print(5==2) #False, because 5 is not equal to 2, performs a comparison operation
print(10 != 10) #False, != means not equal to, but 10 is equal to 10 so it's false
print(2<5) #True, performs a less than operation
print(12>5) #True, performs a greater than operation
print(5<=6) #True, performs a less than or equal to operation
print(1>=10) #False, performs a greater than or equal to operation

x = 5
x += 5 
print(x) #=10
x -= 4
print(x) #=6
x *= 3
print(x) #=18

#Questions and Answers:
#What does the operator and do? Write an expression that reuslts in True. Write an expression that reuslts in False 
#--> The and operator combines 2 conditions and checks if both are true 
six = True
seven = True 
print(six and seven) #True
six = True
eight = False
print (six and eight) #False
#What does the operator or do? Write an expression that results in True. Write an epxerssion that reslts in False
#--> The or operator checks if at least one condiiton is true 
six = True
seven = False
print(six or seven) #True
six = False
eight = False
print(six or eight) #False
#What does the operator not do? Write an epxression that results in True. Write an expression that results in False
#--> The not operator reverses a boolean value, so true becomes false and false becomes true
six = False
print(not six) #True
six = True
print(not six) #False

#More Questions and Answers:
#What is the difference between / and //? --> / performs a divison and // performs a division that rounds down to the nearest lowest whole number
#What is the difference between % and //? --> // performs a divions division that rounds down to the nearest whole number and % returns the remainder after division
#What operator would you use to calculate the remainder when dividing 2 numbers? Give an example
#--> Would use the operator %, 
print(10%3) #=1
#How do assignment operators work? --> Assignment operators assign a value to a vairbale using the = sign

my_string = "hello"
print(my_string) #Prints: hello
print(my_string[0]) #Prints: h
print(my_string[1]) #Prints: e
print(my_string[2]) #Prints: l
print(my_string[3]) #Prints: l
print(my_string[4]) #Prints: o
print(my_string[-1]) #Prints: o
print(my_string[1:3]) #Prints: el 
print(my_string[0:5:2]) #Prints: hlo
print(len(my_string)) #Prints: 5
print(my_string + "goodbye") #Prints: hellogoodbye 
print(7*my_string) #Prints: hellohellohellohellohellohellohello

#Questions and Answers:
#Define the term slicing. For which of the manipulations did you slice your string?
#--> Slicing is a way to extract a portion of the sequence. The manipulations that were sliced are my_string[1:3] and my_string[0:5:2]
#Call the following, describe the result
name = "Oski"
print("Helo, my name is", name) #Prints "Hello my name is Oski"
#Call the following, describe the result
name = "Oski"
print(f"Hello, my name is {name}") #Prints "Hello my name is Oski"
#What is the difference between the last 2 prints? 
#--> The first statement passes multiple values to print() which adds a space between them, the 2nd is an f-string, which inserts variables directly into the string before printing

#cd
# Changes directories. Use it to move from one folder to another
#Example: cd Desktop 
#ls 
#Lists files and folders in the current direcotry 
#Example: ls 
#ls -a
#Lists all files, including hidden files
#Example: ls -a
#mkdir 
#Creates a new directory (folder)
#Example: mkdir example_folder
#cat 
#Displayes the contents of a file in the terminal 
#Example: cat hw1_folder.png
#pwd
#Prints the current working directory (where you are)
#Example: pwd
#cd .. 
#Moves up one directory
#Example cd ..
#cd . 
#Stays in the current directory 
#Example: cd . 
#cp
#Copies files or directories
#Example: cp example_file.txt
#mv
#Moves or renames files or directories
#Example: mv oldname.txt newname.txt
#rm 
#Deletes files or directories permantently 
#Example: rm example_file.txt
#clear 
#Clears the terminal screen
#Example: clear
#grep
#Searches for text inside files
#Example: grep "hello" example_file.text

#Questions and Answers: 
#Look up 3 commands not present. Define and explain how to use them on the command line
#1) touch, creates a new empty file or updates the timestamp of an existing file
#2) echo, prints text to the terminal or writes text into a file
#3) man, displays the manual (help page) for a command
#What is the difference bewteen ls and ls-a? --> ls lists only visible files while ls -a lists all files including any hidden files
#What is a hidden file? --> a file whose name starts with a . and is not shown by deafult when using ls (exluded from default directory)
#Look up 3 other flags. Define and explain how to use them on the command line
#1) ls -l, displays files in log format, showing permissions, owner, size, and date
#2) cp -r, copies directories and their contents recursively 
#3) rm -i, removes the specific direcotry 


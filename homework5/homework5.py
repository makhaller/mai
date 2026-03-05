#3.1 Vocabulary Review
#(1) Git vs. Github
#Git = a distributed version control system used to track changes in code locally
#Github = A platform that hosts Git repositories and allows collaboration
#(2) Terminal vs. Command line
#Terminal = an application used to interact with the computer using text commands
#Command line = the text-based interface where commands are typed and executed
#(3) Local vs. Remote Repository 
#Local = a git repository stored on your own computer 
#Remote = a repository stored online (like GitHub) that can be shared with others
#(4) Version control = a system that records changes to files over time so you can track history and revert to earlier versions 
#(5) Staging Area = a place where changes are prepared before being comitted to the Git repository 
#(6) git add = adds file changes ot the staging area so they can be included in the next commit
#(7) git commit = saves staged changes to the local repository with a message describing the changes
#(8) git push = uploads commits from the local repository to a remote repository 
#(9) git status = shows the current state of the repository, inclduing staged, unstaged, and untracked files 
#(10) git pull = downlaods changes from a remote repository and merges them into the local repository 
#(11) pwd = prints the current working directory (the folder you are currently in)
#(12) ls = lists the files and directories in the current directory 
#(13) cd = changes the current directory to another directory 
#(14) nano = a simple command-line text editor used to create and edit files 
#(15) touch = creates a new empty file
#(16) mv = moves or renames a file or directory
#(17) rm = deletes a file or directory 
#(18) displays the contents of a file in the termianl 

#3.2 A Directory Tree
#pwd 
#ls 
#cd .../ brianna_repo and git pull
#mv homework.py ../python_decal/homework
#cd ../python_decal/homework
#cat homework.py
#git add homework.py, git commit -m "Finished homework", and git push 
#git pull and git push, meaning of error --> the remote repository has commits that Judy does not have locally, so it rehected the push 
#cd ~/ recent 

#4.1 Data Types
def checkDataType(x):
    return type(x).__name__
print(checkDataType(3.14))
print(checkDataType(True))
print(checkDataType(5))
print(checkDataType("hello")) 

#4.2 Conditionals 
def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else: 
        return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(42))

#5 Loops
def sumwithloop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total 
numbers = [1, 2, 3, 4, 5]
print(sumwithloop(numbers))

#6.1 Lists
def duplicatelist(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list
print(duplicatelist(['a', 'b', 'c']))

#6.2 Debugging 
def square(num):
    return num * num 
print(square(4))

#7.2 Favorite Function
def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(42))
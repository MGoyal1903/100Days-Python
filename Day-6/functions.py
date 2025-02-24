'''
Simple Function
Define and call a simple function greet_user which takes name as a parameter. 
The function should print 'Hello, name' to the console.

Default and Keyword Arguments
Update the greet_user function by adding a default value 'Guest' for the name parameter. 
When the function is called without an argument it should print 'Hello, Guest' 
to the console.

Function with Return Values
Write a function that calculates and returns the area of a rectangle. 
The function should take length and breadth as the arguments.
'''

#Prog-1 Greet Users
def greet_user(name):
    print(f"Hello, {name}")
name = input("Enter your name: ")
greet_user(name)


#Prog-2 without arrgument
def greet_users_without_arrguments():
    guest = "jhgds"
    print(f"Hello, {guest}")
greet_users_without_arrguments()


#Prog-3 Area of rectangle
def area_rectangle(length, breath):
    area = length*breath
    return area
length = int(input("Enter the length: "))
breath = int(input("Enter the breath: "))
print(area_rectangle(length,breath))
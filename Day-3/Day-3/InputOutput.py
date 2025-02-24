'''
Basic Input and Output:
Write a program that reads a single input from the user and prints it to the console. 
For example, if the user enters their name, the program should 
output: ""Hello, {name}""
'''

name = input("Enter your Name: ")
print(f"Hello, {name}")

'''
Handling Different Data Types:
Extend the program to read and print different types of inputs. 
Ensure the inputs are properly converted to their respective types and then printed. 
The program should ask the user to enter:

A string
An integer
A floating-point number
'''

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your height in inches: "))

print(f"Name: {name} {type(name)}")
print(f"Age: {age} {type(age)}")
print(f"Height: {height} {type(height)}")

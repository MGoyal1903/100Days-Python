'''
If-else Statements
Write a program that takes an integer as input and checks if it's even or odd.
Write a program that takes an age as input and determines if the person is a child, 
teenager, adult, or senior citizen.
'''

#Prog-1 Even/Odd

num = int(input("Enter any number: "))
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


#Prog-2 Age Checker

age = int(input("Enter your Age: "))
if age <= 12:
    print("you are a child")
elif age<=18 and age>12:
    print("you are a teenager")
elif age<=60 and age>18:
    print("you are an adult")
else:
    print("you are a senior citizen")
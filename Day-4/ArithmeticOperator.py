'''
Arithmetic Operators
Write a program to perform the following arithmetic operations using two numbers:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Exponentiation (**)
'''

def Addition(x,y):
    return x+y 

def Subtraction(x,y):
    return x+y 

def Multiplication(x,y):
    return x+y 

def Division(x,y):
    return x+y 

def Floor_Division(x,y):
    return x+y 

def Modulus(x,y):
    return x+y 

def Exponentiation(x,y):
    return x+y 

if __name__ == '__main__':

    x = int(input("Enter the First number: "))
    y = int(input("Enter the Second number: "))
    action = input("Enter the action you want to perform + , - , * , / , // , % , ** : ")

    
    if action == '+':
        print(Addition(x,y))
    elif action == '-':
        print(Subtraction(x,y))
    elif action == '*':
        print(Multiplication(x,y))
    elif action == '/':
        print(Division(x,y))
    elif action == '//':
        print(Floor_Division(x,y))
    elif action == '%':
        print(Modulus(x,y))
    elif action == '**':
        print(Exponentiation(x,y))

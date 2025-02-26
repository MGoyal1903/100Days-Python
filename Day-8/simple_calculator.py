'''
Day 8: Simple Calculator
Create a simple calculator program that can 
add, subtract, multiply, and divide two integers
'''

add = lambda num1,num2: num1+num2
sub = lambda num1,num2: num1-num2
multi = lambda num1,num2: num1*num2
divide = lambda num1,num2: num1/num2


if __name__ == '__main__':
    print("Welcome to the Simple Calculator: ")
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
    while True:
        action = input("What you want Add(+), Sub(-), Multi(*), Divide(/), Press q for Quit: ")

        if action == '+':
            print(add(num1,num2))
        elif action == '-':
            print(sub(num1,num2))
        elif action == '*':
            print(multi(num1,num2))
        elif action == '/':
            print(divide(num1,num2))
        elif action == 'q':
            print("Exiting")
            exit()

        const = input("Do you wish to continue: Y/N").lower()
        if const == 'n':
            exit()
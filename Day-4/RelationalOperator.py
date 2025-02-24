'''
Relational Operators
Write a program to compare two numbers using the following operators:
Equal to (==)
Not equal to (!=)
Greater than (>)
Less than (<)
Greater than or equal to (>=)
Less than or equal to (<=)
'''

Equal =  lambda x,y: True if x == y else False
Not_Equal = lambda x,y: True if x!= y else False
Greater_than = lambda x,y: True if x>y else False
Less_than = lambda x,y: True if x<y else False
Greater_than_Equal_to = lambda x,y: True if x>=y else False
Less_than_Equal_to = lambda x,y: True if x<=y else False


if __name__ == '__main__':
    x = int(input("Enter the First number: "))
    y = int(input("Enter the Second number: "))
    action = input("Enter the action you want to perform == , != , > , < , >= , <=: ")

    
    if action == '==':
        print(Equal(x,y))
    elif action == '!=':
        print(Not_Equal(x,y))
    elif action == '>':
        print(Greater_than(x,y))
    elif action == '<':
        print(Less_than(x,y))
    elif action == '>=':
        print(Greater_than_Equal_to(x,y))
    elif action == '<=':
        print(Less_than_Equal_to(x,y))

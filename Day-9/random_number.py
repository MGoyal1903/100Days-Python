'''
Day 9: Random number generator
1. Write a program that generates a random number. 
2. Write a program that generates random number between 2 integers
'''

import random
print(f"Random Number: {random.randint(0,100)}")

a = int(input("Enter lower number: "))
b = int(input("Enter upper number: "))

print(f"Random Number between lower and upper is: {random.randint(a,b)}")
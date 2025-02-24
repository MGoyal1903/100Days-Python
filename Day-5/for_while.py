'''
For Loop
Write a program to calculate the sum of all numbers up to the given input number.

While Loop
Write a program to calculate the factorial of a given number.
'''

#Prog-1 Sum of all numbers

num = int(input("Enter any number: "))
sum=0
for i in range(1,num+1):
    sum += i
print(sum)

#Prog-2 Factorial

num1 = int(input("Enter the number: "))
fact = 1
for i in range(1,num1+1):
    fact = fact*i
print(fact)
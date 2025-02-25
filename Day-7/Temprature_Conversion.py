'''
Day 7: Temparature Conversion
1. Write a program to convert temperature from Celsius to Fahrenheit(F = (°C × 9/5) + 32)
2. Write a program to convert temperature from Fahrenheit to Celsius(°C = (°F - 32) × 5/9)
'''

def celsius_to_fahrenheit(celsius):
    f = ((celsius * 9/5) +32)
    return f

def fahrenheit_to_celsius(fahrenheit):
    c = ((fahrenheit-32) * 5/9)
    return c

celsius = int(input("Enter the Temprature in Celsius: "))
fahrenheit = int(input("Enter the Temprature in Fahrenheit: "))

print(celsius_to_fahrenheit(celsius))
print(fahrenheit_to_celsius(fahrenheit))
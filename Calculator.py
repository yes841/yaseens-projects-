# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 14:54:21 2021

@author: yasee
"""

## Simple Calculator 

def add(a,b):
    return a + b


def substract(a,b):
    return a - b


def multiply(a,b):
    return a * b


def divide(a,b):
    return a / b

print("Select Operation :")
print("1: Add")
print("2: Substraction")
print("3: Multiply")
print("4: Divide")

choice = input("Enter choice (1/2/3/4)")

num1 = int(input("Enter first number : "))

num2 = int(input("Enter second number : "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1,num2))
    
elif choice == "2":
    print(num1, "-", num2, "=", substract(num1,num2))
    
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == "4":
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    print("Invalid input")
    
# -*- coding: utf-8 -*-

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = int(a) / int(b)
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")
else:
    print("result squared: ", result ** 2)
"""
Example:

$ python divide_ver3.py
Enter first number: 10
Enter second number: 2
result squared:  25

$ python divide_ver3.py
Enter first number: werq
Enter second number: 3
Something went wrong...
"""

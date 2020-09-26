# -*- coding: utf-8 -*-

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Output: ", int(a) / int(b))
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")

"""
Example:

$ python divide_ver2.py
Enter first number: wer
Enter second number: 4
Output:  Something went wrong...

$ python divide_ver2.py
Enter first number: 5
Enter second number: 0
Output:  Something went wrong...
"""

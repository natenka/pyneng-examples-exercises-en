# -*- coding: utf-8 -*-

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print("Результат: ", int(a) / int(b))
except ValueError:
    print("Please enter only numbers")
except ZeroDivisionError:
    print("You can't divide by zero")

"""
Example:

$ python divide.py
Enter first number: 3
Enter second number: 1
Output:  3

$ python divide.py
Enter first number: 5
Enter second number: 0
Output: You can't divide by zero

$ python divide.py
Enter first number: qewr
Enter second number: 3
Output:  Please enter only numbers
"""

# -*- coding: utf-8 -*-

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    result = int(a) / int(b)
except (ValueError, ZeroDivisionError):
    print("Something went wrong...")
else:
    print("Result squared: ", result ** 2)
finally:
    print("The End")
"""
Example:

$ python divide_ver4.py
Enter first number: 10
Enter second number: 2
Result squared:  25
The End

$ python divide_ver4.py
Enter first number: qwerewr
Enter second number: 3
Something went wrong...
The End

$ python divide_ver4.py
Enter first number: 4
Enter second number: 0
Something went wrong...
The End
"""

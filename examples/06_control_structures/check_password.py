# -*- coding: utf-8 -*-

username = input("Enter username: ")
password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short")
elif username in password:
    print("Password contains username")
else:
    print("Password for user {} is set".format(username))

"""
Usage example:

$ python check_password.py
Enter username: nata
Enter password: nata1234
Password contains username

$ python check_password.py
Enter username: nata
Enter password: 123nata123
Password contains username

$ python check_password.py
Enter username: nata
Enter password: 1234
Password is too short

$ python check_password.py
Enter username: nata
Enter password: 123456789
Password for user nata is set
"""

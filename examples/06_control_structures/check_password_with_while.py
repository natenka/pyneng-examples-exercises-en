# -*- coding: utf-8 -*-

username = input("Enter username: ")
password = input("Enter password: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Пароль слишком короткий\n")
        password = input("Re-enter password: ")
    elif username in password:
        print("Password contains username\n")
        password = input("Re-enter password: ")
    else:
        print("Password for user {} is set".format(username))
        password_correct = True

"""
Example:
$ python check_password_with_while.py
Enter username: nata
Enter password: nata
Пароль слишком короткий

Re-enter password: natanata
Password contains username

Re-enter password: 123345345345
Password for user nata is set
"""

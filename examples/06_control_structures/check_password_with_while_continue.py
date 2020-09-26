username = input("Enter username: ")
password = input("Enter password: ")

password_correct = False

while not password_correct:
    if len(password) < 8:
        print("Password is too short\n")
    elif username in password:
        print("Password contains username\n")
    else:
        print("Password for user {} is set".format(username))
        password_correct = True
        continue
    password = input("Re-enter password: ")

username = input("Enter username: ")
password = input("Enter password: ")

while True:
    if len(password) < 8:
        print("Password is too short\n")
    elif username in password:
        print("Password contains username\n")
    else:
        print("Password for user {} is set".format(username))
        # ends the cycle
        break
    password = input("Re-enter password: ")

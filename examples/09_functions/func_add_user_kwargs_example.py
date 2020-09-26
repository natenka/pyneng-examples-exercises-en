def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        print("Password is too short")
        return False
    elif check_username and username in password:
        print("Password contains username")
        return False
    else:
        print(f"Password for user {username} passed all checks")
        return True


def add_user_to_users_file(user, users_filename="users.txt", **kwargs):
    while True:
        passwd = input(f"Enter the password for the user {user}: ")
        if check_passwd(user, passwd, **kwargs):
            break
    with open(users_filename, "a") as f:
        f.write(f"{user},{passwd}")

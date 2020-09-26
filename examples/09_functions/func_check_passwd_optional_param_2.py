def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Password is too short')
        return False
    elif check_username and username in password:
        print('Password contains username')
        return False
    else:
        print(f"Password for user {username} passed all checks")
        return True


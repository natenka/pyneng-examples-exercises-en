def check_passwd(username, password, min_length=8):
    if len(password) < min_length:
        print('Password is too short')
        return False
    elif username in password:
        print('Password contains username')
        return False
    else:
        print(f"Password for user {username} passed all checks")
        return True




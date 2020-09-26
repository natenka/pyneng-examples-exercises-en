def check_passwd(username, password):
    if len(password) < 8:
        print('Password is too short')
        return False
    elif username in password:
        print('Password contains username')
        return False
    else:
        print(f'Password for user {username} passed all checks')
        return True



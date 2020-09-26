# try/except version
while True:
    a = input("Enter number: ")
    b = input("Enter second number: ")
    try:
        result = int(a) / int(b)
    except ValueError:
        print("Please enter only numbers")
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(result)
        break

# Without try/except
while True:
    a = input("Enter number: ")
    b = input("Enter second number: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("You can't divide by zero")
        else:
            print(int(a) / int(b))
            break
    else:
        print("Please enter only numbers")

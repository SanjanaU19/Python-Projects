try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("What kind of operation do you want to perform?")
    print("Press + for Addition")
    print("Press - for Subtraction")
    print("Press * for Multiplication")
    print("Press / for Division")

    o = input("Enter a operation:")
    match o:
        case"+":
            print(f"The Result is:{a+b}")
        case "-":
            print(f"The Result is {a-b}")
        case"*":
            print(f"The Result is:{a*b}")
        case"/":
            print(f"The Result is:{a/b}")
        case _:
            print(f"There was an error")
            
except Exception as e:
       print("Enter a valid value of a and b:")



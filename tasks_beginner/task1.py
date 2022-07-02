a = int(input("first_number:"))
b = int(input("second_number:"))
operation = input("operation:")
if (operation == "+"):
    print(a+b)
elif (operation == "-"):
    print(a-b)
elif (operation == "*"):
    print(a*b)
elif (operation == "/"):
    print(a/b)
elif (operation == "%"):
    print(a % b)
else:
    print("не верный оператор")
first=input("First NO:")
operator=input("Enter operator(+,-,/,%):")
second=input("Second NO:")
first=int(first)
second=int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
        print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("invalid operation")
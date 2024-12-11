a = int(input("enter a number: "))
b = int(input("enter a number: "))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zero")
else:
    print(F"divison a/b is{a/b}")
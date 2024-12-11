try:
    a = int(input("Hey , enter a number: "))
    print(a)

except ValueError as e:
    print(e)

else:
    print("i am inside else")
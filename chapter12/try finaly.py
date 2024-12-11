try:
    a = int(input("Hey , enter a number: "))
    print(a)

except ValueError as e:
    print(e)

finally:
    print("hey i am inside of finally")

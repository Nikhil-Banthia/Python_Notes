try:
    a = int(input("Abey! ek number enter kar:\n"))

except Exception as e:
    print(e)
except ValueError as e:
    print(e)

print("Thank you")
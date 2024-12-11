#using while loop

n = int(input("ek number enter kar uske factorial ke liye"))
factorial = n

while(n>1):
    factorial = factorial*(n-1)
    n-=1
print(factorial)

#while using for loop

v = int(input("ek number enter kar uske factorial ke liye"))
product = 1
for a in range(1,v+1):
    product = product*a
print(product)
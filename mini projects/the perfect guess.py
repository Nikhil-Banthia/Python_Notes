import random
n = random.randint(1,100)
a = -1
guess = 1
while(a != n):
    
    a = int(input("guess a number: "))
    if(a > n):
        print("lower number please")
        guess += 1
    else:
        print("high number please")
        guess += 1

print(f"you have guessed the number correctly in {guess} attempt")
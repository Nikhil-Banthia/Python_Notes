import random

'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0])
print("choose snake, water or gun")
youstr = input("enter your choice:\n")
youdict = {"snake":1, "water":-1, "gun":0}
reversedict ={1:"snake", -1:"water", 0:"gun"}
you = youdict[youstr]
print(f"you choose:\n{reversedict[you]}\n\ncomputer choose:\n{reversedict[computer]}\n")
# if(computer == -1 and you ==1):
#     print("you Win")
# elif(computer == 1 and you ==0):
#     print("you Win")
# elif(computer == 0 and you ==-1):
#     print("you Win")
# elif(computer == 1 and you ==-1):
#     print("you Lose")
# elif(computer == -1 and you ==0):
#     print("you Lose")
# elif(computer == 0 and you ==1):
#     print("you Lose")
# elif(computer == 0 and you ==0):
#     print("It's a Draw")
# elif(computer == 1 and you ==1):
#     print("It's a Draw")
# elif(computer == -1 and you == -1):
#     print("It's a Draw")
# else:
#     print("something went wrong")
if((computer - you ) == -1 or (computer - you)==2):
    print("You Lose!")
else:
    print("You Win") 
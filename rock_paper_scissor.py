import random

print("--------Enter Your Choice--------")
x=input("Rock,Paper,Scissor: ")
if(x=="Rock"):
    y=0
elif x=="Paper":
    y=1
else :
    y=2       
    
computer_choice=random.randint(0,2)

if computer_choice==0:
    print("Computer choice is Rock")
elif computer_choice==1:
    print("Computer choice is Paper")
else :
    print("Computer choice is Scissor")        

if y==0 and computer_choice==2:
    print("You Win")
elif y==2 and computer_choice==0:
    print("You Lose")
elif y==1 and computer_choice==2:
    print("You Lose")
elif y==2 and computer_choice==1:
    print("You Win")
elif y==0 and computer_choice==1:
    print("You Lose")
elif y==1 and computer_choice==0:
    print("You Win")
elif y==computer_choice:
    print("Its a Draw")                             

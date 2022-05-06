#rock paper scissor game
import random
c1=0
c2=0
draw=0
a='y'
user=input("Enter your name: ")
while a=='y':
    print("Rock for 1\nPaper for 2\nScissor for 3 ")
    U1=int(input("Enter a choice: "))
    U2=random.randint(1,3)
    print("Computer choiced:",U2)
    if(1<=U1<=3):
        if((U1==1 and U2==3)):
            print("U1 Wins")
            c1=c1+1;
        elif((U1==3 and U2==2)):
            print("U1 Wins")
            c1=c1+1;
        elif((U1==2 and U2==1)):
            print("U1 Wins")
            c1=c1+1;
        elif((U2==1 and U1==3)):
            print("U2 Wins")
            c2=c2+1;
        elif((U2==3 and U1==2)):
            print("U2 Wins")
            c2=c2+1;
        elif((U2==2 and U1==1)):
            print("U2 Wins")
            c2=c2+1;
        else:
            print("Draw")
            draw=draw+1
    else:
        print("Invalid Input from user!!!")
    a=str.lower(input("Do you want to play again (y/n): "))
if(c1>c2):
    print("Final Result:-\n congratulation",user,"!!! ,You won the match And you wins",c1,"games out of ",c1+c2+draw,"games")
elif(c1<c2):
    print("Final Result:-\n User2(computer) is Winner of the match And It wins",c2,"games out of ",c1+c2+draw,"games")
else:
    print("Final Result:-\n Match is Draw!!! Both wins",c1,"-",c2,"Games and",draw,"games are draw")


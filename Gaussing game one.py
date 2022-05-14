#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the
#number, then tell them whether they guessed too low, too high, or exactly right.
guess=0
right=0
end = 1
while(end!="exit"):
    import random

    i=random.randint(1,9)

    n=int(input("Guess a Number between 1 to 9: "))
    guess += 1
    print("Random number by computer: ",i)
    print()
    if(i==n):
        print("Guessing is right.")
        right += 1
    elif(i>n):
        print("Guessing is too low")
    else:
        print("Guessing is too high")
    print()
    end=input("Enter 'exit' to end game or Enter not exit: ")
    print()
print(f"You Guessed {guess} time And Your Guessing is right {right} time")


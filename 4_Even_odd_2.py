#python.org
'''Problem: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by
(check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.'''


import time
initial=time.time()
a=int(input("Enter a number: "))
if(a%2==0):
    print("Number is even")
    if(a%4==0):
        print("Number is multiple of 4")
else:
    print("Number is odd")
b=int(input("Enter a number to check: "))
c=int(input("Enter a number to divide: "))
if(b%c==0):
    print(b," divides evenly by ",c)
else:
    print(b," does not divide evenly by ",c)
print("Time required for program is:",time.time()-initial)


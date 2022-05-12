#create a program to find the factorial of a user defined integer with iterative method

print("Program to find factorial of a positive number.")

a=int(input("Enter a number to factorial: "))
fact_pos=1
if(a>0):
    for i in range(1,a+1):
        fact_pos=fact_pos*i
    print(str(a)+"! =",str(fact_pos))
else:
    print("Please provide positive number!!!")


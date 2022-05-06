#prime number
a=int(input("Enter a number: "))

if(a>=2):
    for i in range(2,a//2+1):
        if(a%i==0):
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")
else:
    print("Invalide value!!!")
        

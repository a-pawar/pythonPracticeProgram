#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

a=input("Enter a string: ")
print(a)

n=len(a)
flag=0
for i in range(0,n//2):
    if(a[i]==a[n-i-1]):
        flag=1
    else:
        flag=0
        break

if(flag):
    print(f"{a} is palindrome.")
else:
    print(f"{a} is NOT palindrome.")

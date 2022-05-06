#string reverse
#str1="Anshul Pawar"
str1=input("Enter a string: ")
c=len(str1)
print(c)
#s=""
#for i in range(c-1,-1,-1):
#    s+=str1[i]
#print(s)

#for i in range(0,c//2):
#    a=str1[i]
#    str1[i]=str1[c-i-1]
#    str1[c-i-1]=a
print(str1)
#through error because string are immutable

str1=str1[::-1]
print(str1)

str2="Anshul"[::-1]
print(str2)



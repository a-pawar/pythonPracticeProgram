#String function

str1="I am fine"
print(str1)
x=len(str1)
print(x)

print("Length of str1 = ",x)
print("Length of str1 = "+str(x))
print("Length of str1 ={}".format(x))



y=str1.index("a")
print(y)
#print reverse
for i in range(x-1,-1,-1):
    print(str1[i],end=' ')
    print(i)

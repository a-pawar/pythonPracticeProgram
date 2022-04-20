#Greater of three number
a=int(input("Enter a 1st number: "))
b=int(input("Enter a 2nd number: "))
c=int(input("Enter a 3rd number: "))

if(a==b==c):
    print("All are Equal")

elif((a>b) and (a>c)):
      print(a, "is greater")
elif((b>c) and (b>a)):
      print(b, "is greater")
elif((c>a) and (c>b)):
      print(c, "is greater")
elif((a==c) and (a<b)):
    print(a,"and",c,"are equal",b,"is greater")
elif((a==b) and (a<c)):
    print(a,"and",b,"are equal",c,"is greater")
elif((a==c) and (a>b)):
    print(a,"and",c,"are equal and greater",b,"is smaller")
elif((a==b) and (a>c)):
    print(a,"and",b,"are equal and greater",c,"is smaller")
elif((b==c) and (b<a)):
    print(b,"and",c,"are equal",a,"is greater")
elif((b==c) and (b>a)):
    print(b,"and",c,"are equal and greater",a,"is smaller")





   
